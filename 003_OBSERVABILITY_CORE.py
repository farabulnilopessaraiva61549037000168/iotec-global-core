"""
===============================================================================
003_OBSERVABILITY_CORE.py
Centro de InteligÃªncia de Observabilidade da IOTEC
===============================================================================
"""

from datetime import datetime


class Observatory:

    def __init__(self):

        self.logs = []

        self.metrics = {

            "missions":0,

            "products":0,

            "clients":0,

            "payments":0,

            "errors":0,

            "alerts":0

        }

    # ----------------------------------------------------------------------

    def receive(self,event):

        log={

            "time":datetime.now(),

            "event":event.name,

            "data":event.data

        }

        self.logs.append(log)

        self.process(log)

    # ----------------------------------------------------------------------

    def process(self,log):

        event=log["event"]

        if event=="MISSION_CREATED":

            self.metrics["missions"]+=1

        elif event=="PRODUCT_READY":

            self.metrics["products"]+=1

        elif event=="CLIENT_FOUND":

            self.metrics["clients"]+=1

        elif event=="PAYMENT_RECEIVED":

            self.metrics["payments"]+=1

        elif event=="ERROR":

            self.metrics["errors"]+=1

        elif event=="ALERT":

            self.metrics["alerts"]+=1

    # ----------------------------------------------------------------------

    def dashboard(self):

        print()

        print("="*70)

        print("IOTEC LIVE OBSERVABILITY")

        print("="*70)

        print()

        print(f"MissÃµes............. {self.metrics['missions']}")

        print(f"Produtos............ {self.metrics['products']}")

        print(f"Clientes............ {self.metrics['clients']}")

        print(f"Pagamentos.......... {self.metrics['payments']}")

        print(f"Erros............... {self.metrics['errors']}")

        print(f"Alertas............. {self.metrics['alerts']}")

        print()

    # ----------------------------------------------------------------------

    def timeline(self):

        print()

        print("="*70)

        print("TIMELINE")

        print("="*70)

        print()

        for log in self.logs:

            hora=log["time"].strftime("%H:%M:%S")

            print(f"{hora}  {log['event']}")

        print()


# =============================================================================
# TESTE
# =============================================================================

if __name__=="__main__":

    class Event:

        def __init__(self,name,data=None):

            self.name=name

            self.data=data or {}

    obs=Observatory()

    obs.receive(Event("MISSION_CREATED"))

    obs.receive(Event("MISSION_CREATED"))

    obs.receive(Event("CLIENT_FOUND"))

    obs.receive(Event("PRODUCT_READY"))

    obs.receive(Event("PAYMENT_RECEIVED"))

    obs.receive(Event("PAYMENT_RECEIVED"))

    obs.receive(Event("ALERT"))

    obs.dashboard()

    obs.timeline()

