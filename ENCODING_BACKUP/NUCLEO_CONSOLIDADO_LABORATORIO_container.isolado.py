import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# CriaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o do DÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚ÂjÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â EstÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©reo com container isolado
docker run -d \
  --name dojo_estereo \
  --network=isolado_ninja \
  --env VAR_AMBIENTE=oculto \
  --mount type=tmpfs,destination=/dados_temporarios \
  ninja_sistema:ultima_versao



