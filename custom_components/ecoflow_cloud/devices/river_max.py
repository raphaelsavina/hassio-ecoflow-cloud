from . import const, BaseDevice
from ..entities import BaseSensorEntity, BaseNumberEntity, BaseSwitchEntity, BaseSelectEntity
from ..mqtt.ecoflow_mqtt import EcoflowMQTTClient
from ..number import MaxBatteryLevelEntity
from ..select import DictSelectEntity
from ..sensor import LevelSensorEntity, WattsSensorEntity, RemainSensorEntity, TempSensorEntity, \
    CyclesSensorEntity, InWattsSensorEntity, OutWattsSensorEntity
from ..switch import EnabledEntity, BeeperEntity


class RiverMax(BaseDevice):
    def sensors(self, client: EcoflowMQTTClient) -> list[BaseSensorEntity]:
        return [
            LevelSensorEntity(client, "pd.soc", const.MAIN_BATTERY_LEVEL),
            WattsSensorEntity(client, "pd.wattsInSum", const.TOTAL_IN_POWER),
            WattsSensorEntity(client, "pd.wattsOutSum", const.TOTAL_OUT_POWER),

            InWattsSensorEntity(client, "inv.inputWatts", const.AC_IN_POWER),

            OutWattsSensorEntity(client, "inv.outputWatts", const.AC_OUT_POWER),
            OutWattsSensorEntity(client, "pd.carWatts", const.DC_OUT_POWER),

            OutWattsSensorEntity(client, "pd.typecWatts", const.TYPEC_OUT_POWER),

            OutWattsSensorEntity(client, "pd.usb1Watts", const.USB_1_OUT_POWER),
            OutWattsSensorEntity(client, "pd.usb2Watts", const.USB_2_OUT_POWER),
            OutWattsSensorEntity(client, "pd.usb3Watts", const.USB_3_OUT_POWER),

            RemainSensorEntity(client, "pd.remainTime", const.REMAINING_TIME),
            TempSensorEntity(client, "bmsMaster.temp", const.BATTERY_TEMP),
            CyclesSensorEntity(client, "bmsMaster.cycles", const.CYCLES),

            LevelSensorEntity(client, "bmsSlave1.soc", const.SLAVE_BATTERY_LEVEL, False, True),
            TempSensorEntity(client, "bmsSlave1.temp", const.SLAVE_BATTERY_TEMP, False, True),
            CyclesSensorEntity(client, "bmsSlave1.cycles", const.SLAVE_CYCLES, False, True)
        ]

    def numbers(self, client: EcoflowMQTTClient) -> list[BaseNumberEntity]:
        return [
            MaxBatteryLevelEntity(client, "bmsMaster.maxChargeSoc", const.MAX_CHARGE_LEVEL, 50, 100, None),
            # MinBatteryLevelEntity(client, "bmsMaster.minDsgSoc", const.MIN_DISCHARGE_LEVEL, 0, 30, None),
        ]

    def switches(self, client: EcoflowMQTTClient) -> list[BaseSwitchEntity]:
        return [
            BeeperEntity(client, "pd.beepState", const.BEEPER, lambda value: {"moduleType": 0, "operateType": "TCP", "params": {"id": 38, "enabled": value}}),
            EnabledEntity(client, "inv.cfgAcEnabled", const.AC_ENABLED, lambda value: {"moduleType": 0, "operateType": "TCP", "params": {"id": 66, "enabled": value}}),
            EnabledEntity(client, "pd.carSwitch", const.DC_ENABLED, lambda value: {"moduleType": 0, "operateType": "TCP", "params": {"id": 34, "enabled": value}}),
            EnabledEntity(client, "inv.cfgAcXboost", const.XBOOST_ENABLED, lambda value: {"moduleType": 0, "operateType": "TCP", "params": {"id": 66, "xboost": value}})

        ]

    def selects(self, client: EcoflowMQTTClient) -> list[BaseSelectEntity]:
        return [

            DictSelectEntity(client, "pd.standByMode", const.UNIT_TIMEOUT, const.UNIT_TIMEOUT_OPTIONS, lambda value: {"moduleType": 0, "operateType": "TCP", "params": {"id": 33, "standByMode": value}}),
            DictSelectEntity(client, "inv.cfgStandbyMin", const.AC_TIMEOUT, const.AC_TIMEOUT_OPTIONS, lambda value: {"moduleType": 0, "operateType": "TCP", "params": {"id": 153, "standByMins": value}}),

        ]
