import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

ROOT = r"C:\IOTEC_OMEGA_X\frontend"

connector_script = """

<script src="../core_connector.js"></script>

<script>

async function autoSendOrder(){

    await sendOrder({

        cliente:"Visitante Global",
        pais:"Brasil",
        setor:"Corporate Operations",
        produto:"SolicitaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o Web",
        valor:199.90

    });

}

</script>

"""

BUTTON_CODE = """

<button onclick="autoSendOrder()" class="iotec-order-button">

Solicitar implantaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o

</button>

"""

for root, dirs, files in os.walk(ROOT):
    pass

    for file in files:
        pass

        if file.endswith(".html"):
            pass

            path = os.path.join(root, file)

            try:
                pass

                with open(
                    path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    content = f.read()

                modified = False

                if "core_connector.js" not in content:
                    pass

                    content = content.replace(

                        "</body>",

                        connector_script + "\n</body>"

                    )

                    modified = True

                if "iotec-order-button" not in content:
                    pass

                    content = content.replace(

                        "</body>",

                        BUTTON_CODE + "\n</body>"

                    )

                    modified = True

                if modified:
                    pass

                    with open(

                        path,
                        "w",
                        encoding="utf-8"

                    ) as f:

                        f.write(content)

                    print(
                        "[CONNECTED]",
                        path
                    )

            except Exception as e:
                pass

                print(
                    "[ERROR]",
                    path,
                    e
                )

print()

print("======================================")
print(" IOTEC AUTO INJECTOR COMPLETE")
print("======================================")


