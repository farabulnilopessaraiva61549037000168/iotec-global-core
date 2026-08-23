import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import boto3
import os

class OmegaAWS:
    def __init__(self):
        self.access_key = os.getenv('AWS_ACCESS_KEY_ID')
        self.secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        self.session = boto3.Session(
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key
        )
        self.ec2 = self.session.client('ec2')
        self.s3 = self.session.client('s3')

    def check_balance(self):
        # Pseudo-cÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digo. Precisa de conexÃƒÆ'Ã†â€™o com Billing API (faturamento AWS)
        print("Consultando saldo...")
        # Se saldo exceder limite, dispara shutdown
        return "Saldo dentro dos limites Free Tier."

    def create_ec2_instance(self):
        print("Criando InstÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ncia EC2...")
        response = self.ec2.run_instances(
            ImageId='ami-xxxxxxxx', # Escolher AMI correta
            InstanceType='t3.micro',
            MinCount=1,
            MaxCount=1
        )
        print("InstÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ncia criada:", response)
        return response

    def shutdown_all_instances(self):
        print("Desligando todas as instÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ncias...")
        instances = self.ec2.describe_instances()
        ids = []
        for res in instances['Reservations']:
            for inst in res['Instances']:
                ids.append(inst['InstanceId'])
        if ids:
            self.ec2.terminate_instances(InstanceIds=ids)
            print("InstÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ncias encerradas:", ids)
        else:
            print("Nenhuma instÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ncia para desligar.")

# Exemplo de uso
if __name__ == "__main__":
    omega = OmegaAWS()
    print(omega.check_balance())
    omega.create_ec2_instance()
    # omega.shutdown_all_instances() # Ativa quando quiser encerrar tudo


