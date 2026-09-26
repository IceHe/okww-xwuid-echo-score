"""Reconnect an active OK Script capture after the game process is restarted."""

import logging
import threading
import time


logger = logging.getLogger(__name__)


class CaptureRecoveryMonitor:
    def __init__(self, device_manager, exit_event, interval=1.0, retry_delay=5.0):
        self.device_manager = device_manager
        self.exit_event = exit_event
        self.interval = interval
        self.retry_delay = retry_delay
        self._last_attempt = float("-inf")
        self._last_hwnd = 0
        self._stop_event = threading.Event()
        self._thread = None

    def start(self):
        if self._thread is None:
            self._thread = threading.Thread(
                target=self._run, name="EchoCaptureRecovery", daemon=True,
            )
            self._thread.start()

    def stop(self):
        self._stop_event.set()

    def _run(self):
        while not self.exit_event.is_set() and not self._stop_event.wait(self.interval):
            try:
                self.poll()
            except Exception:
                logger.exception("Echo capture recovery check failed")

    def poll(self):
        """Retry only an already-started capture with a currently valid game HWND."""
        manager = self.device_manager
        if manager is None or self.exit_event.is_set() or self._stop_event.is_set():
            return False

        window = getattr(manager, "hwnd_window", None)
        hwnd = getattr(window, "hwnd", 0) if getattr(window, "exists", False) else 0
        if not hwnd:
            self._last_hwnd = 0
            return False

        executor = getattr(manager, "executor", None)
        capture = getattr(manager, "capture_method", None)
        if executor is None or executor.paused:
            return False
        if capture is not None and capture.connected():
            self._last_hwnd = hwnd
            return False

        now = time.monotonic()
        if hwnd == self._last_hwnd and now - self._last_attempt < self.retry_delay:
            return False
        self._last_hwnd = hwnd
        self._last_attempt = now
        # DeviceManager.start() schedules a normal capture reinitialization on
        # its own handler. The scoring TriggerTask cannot do this: OK Script
        # skips triggers while there is no connected capture/frame.
        logger.info("Reconnecting Echo capture for game HWND %s", hwnd)
        manager.start()
        return True
