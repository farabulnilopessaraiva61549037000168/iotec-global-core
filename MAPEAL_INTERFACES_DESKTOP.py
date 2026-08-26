import os

class DesktopInterfaceScanner:
    def __init__(self):
        self.user_profile = os.path.expanduser("~")
        self.target_dir = os.path.join(self.user_profile, "Desktop", "Diversos", "INTERFACES")

    def escanear(self):
        print("==========================================================================================")
        print(f" 📂 MAPEANDO ACERVO TÉCNICO EM: {self.target_dir}")
        print("==========================================================================================")

        if not os.path.exists(self.target_dir):
            print(" ⚠️ Pasta não localizada no caminho padrão do Desktop. Verificando variações...")
            # Busca alternativa na Area de Trabalho em portugues/ingles
            desktop_pt = os.path.join(self.user_profile, "Área de Trabalho", "Diversos", "INTERFACES")
            if os.path.exists(desktop_pt):
                self.target_dir = desktop_pt
            else:
                print(" ❌ Não foi possível encontrar a pasta 'Diversos/INTERFACES' automaticamente.")
                return

        total_arquivos = 0
        modulos_encontrados = []

        for root, dirs, files in os.walk(self.target_dir):
            for file in files:
                total_arquivos += 1
                ext = os.path.splitext(file)[1].lower()
                path_rel = os.path.relpath(os.path.join(root, file), self.target_dir)
                modulos_encontrados.append((file, ext, path_rel))

        print(f" ✅ Sucesso! Encontrados {total_arquivos} arquivos de interface e complemento técnico:\n")
        
        # Categorização rápida
        for nome, ext, rel in modulos_encontrados:
            tipo = "🌐 Web / HTML" if ext in ['.html', '.htm'] else "🎨 Estilo / Assets" if ext in ['.css', '.png', '.jpg', '.svg', '.mp4'] else "⚙️ Código / Script"
            print(f"   • [{tipo}] {rel}")

        print("\n==========================================================================================")
        print(" 🚀 Mapeamento concluído! Prontos para selecionar os complementos do Showroom.")
        print("==========================================================================================")

if __name__ == "__main__":
    scanner = DesktopInterfaceScanner()
    scanner.escanear()
