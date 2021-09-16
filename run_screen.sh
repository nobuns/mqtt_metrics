#!/bin/bash
if ! screen -list | grep -q "pnp_device"; then
    screen -dmS pnp_device python telemetry_pnp.py
fi


