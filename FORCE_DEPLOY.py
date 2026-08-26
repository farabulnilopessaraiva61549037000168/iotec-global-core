import subprocess
cmd = 'npx netlify-cli deploy --site 58fbf9c1-d40f-4c70-b723-e2d066a5fd43 --dir dist --prod'
subprocess.run(cmd, shell=True)
