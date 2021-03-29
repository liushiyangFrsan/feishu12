# -*- coding: UTF-8 -*-
# Code generated by lark suite oapi sdk gen

from typing import Callable

from ....config import Config
from ....context import Context
from ....event.event import set_event_callback

from .model import *


class AppOpenEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, AppOpenEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, AppOpenEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, AppOpenEvent], Any]) -> None
        handler = AppOpenEventHandler(callback)
        set_event_callback(conf, "app_open",
                          handler.handle, clazz=AppOpenEvent)


class AppStatusChangeEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, AppStatusChangeEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, AppStatusChangeEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, AppStatusChangeEvent], Any]) -> None
        handler = AppStatusChangeEventHandler(callback)
        set_event_callback(conf, "app_status_change",
                          handler.handle, clazz=AppStatusChangeEvent)


class AppUninstalledEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, AppUninstalledEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, AppUninstalledEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, AppUninstalledEvent], Any]) -> None
        handler = AppUninstalledEventHandler(callback)
        set_event_callback(conf, "app_uninstalled",
                          handler.handle, clazz=AppUninstalledEvent)


class OrderPaidEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, OrderPaidEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, OrderPaidEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, OrderPaidEvent], Any]) -> None
        handler = OrderPaidEventHandler(callback)
        set_event_callback(conf, "order_paid",
                          handler.handle, clazz=OrderPaidEvent)
