import os

os.system("openxlab model download --model-repo 'fiv/DreamBinaryAssistant_Merge'")
os.system('git clone https://github.com/InternLM/InternLM.git && '
          'cp app.py InternLM/ && '
          'streamlit run InternLM/app.py --server.address=0.0.0.0 --server.port 7860')
