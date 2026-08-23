import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
AGENTS = [

"DISCOVERY_ENGINE",
"MAPS_ENGINE",
"LINKEDIN_ENGINE",
"INSTAGRAM_ENGINE",
"EMAIL_ENGINE",
"PROPOSAL_ENGINE",
"PAYMENT_ENGINE",
"MISSION_CONTROL"

]



