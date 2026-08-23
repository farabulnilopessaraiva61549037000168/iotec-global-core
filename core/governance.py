import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

import shutil



from datetime import datetime





class GovernanceEngine:
    pass



    def __init__(self):
        pass



        self.logs = []



        self.backup_directory = (

            "backups"

        )



        if not os.path.exists(

            self.backup_directory

        ):



            os.makedirs(

                self.backup_directory

            )



    def backup_file(

        self,

        filepath

    ):



        if not os.path.exists(filepath):
            pass



            print("\n[BACKUP]")



            print("FILE NOT FOUND")



            return



        timestamp = datetime.now().strftime(

            "%Y%m%d_%H%M%S"

        )



        filename = os.path.basename(

            filepath

        )



        backup_name = (

            f"{timestamp}_{filename}"

        )



        backup_path = os.path.join(

            self.backup_directory,

            backup_name

        )



        shutil.copy2(

            filepath,

            backup_path

        )



        print("\n[BACKUP]")



        print(

            f"BACKUP CREATED: "

            f"{backup_name}"

        )




