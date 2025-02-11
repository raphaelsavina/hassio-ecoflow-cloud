## RIVER_MAX

*Sensors*
- Main Battery Level (`pd.soc`)
- Total In Power (`pd.wattsInSum`)
- Total Out Power (`pd.wattsOutSum`)
- AC In Power (`inv.inputWatts`)
- AC Out Power (`inv.outputWatts`)
- DC Out Power (`pd.carWatts`)
- Type-C Out Power (`pd.typecWatts`)
- USB (1) Out Power (`pd.usb1Watts`)
- USB (2) Out Power (`pd.usb2Watts`)
- USB (3) Out Power (`pd.usb3Watts`)
- Remaining Time (`pd.remainTime`)
- Battery Temperature (`bmsMaster.temp`)
- Cycles (`bmsMaster.cycles`)
- Slave Battery Level (`bmsSlave1.soc`)
- Slave Battery Temperature (`bmsSlave1.temp`)
- Slave Cycles (`bmsSlave1.cycles`)

*Switches*
- Beeper (`pd.beepState` -> `{"moduleType": 0, "operateType": "TCP", "params": {"id": 38, "enabled": "VALUE"}}`)
- AC Enabled (`inv.cfgAcEnabled` -> `{"moduleType": 0, "operateType": "TCP", "params": {"id": 66, "enabled": "VALUE"}}`)
- DC (12V) Enabled (`pd.carSwitch` -> `{"moduleType": 0, "operateType": "TCP", "params": {"id": 34, "enabled": "VALUE"}}`)
- X-Boost Enabled (`inv.cfgAcXboost` -> `{"moduleType": 0, "operateType": "TCP", "params": {"id": 66, "xboost": "VALUE"}}`)

*Sliders (numbers)*
- Max Charge Level (`bmsMaster.maxChargeSoc` -> `_ command not available _` [50 - 100])

*Selects*
- Unit Timeout (`pd.standByMode` -> `{"moduleType": 0, "operateType": "TCP", "params": {"id": 33, "standByMode": "VALUE"}}` [Never (0), 30 min (30), 1 hr (60), 2 hr (120), 4 hr (240), 6 hr (360), 12 hr (720), 24 hr (1440)])
- AC Timeout (`inv.cfgStandbyMin` -> `{"moduleType": 0, "operateType": "TCP", "params": {"id": 153, "standByMins": "VALUE"}}` [Never (0), 30 min (30), 1 hr (60), 2 hr (120), 4 hr (240), 6 hr (360), 12 hr (720), 24 hr (1440)])


