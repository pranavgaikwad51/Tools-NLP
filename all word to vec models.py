! pip install gensim # if this do not work forcefully install the gensim in your IDE

# Forcefully installation 👇🏻 - if upper code does not work 

! pip install gensim --no-cache-dir numpy gensim scipy

# -------IN Some cases the older model is installed then upgrade the gensim---------

! pip install --upgrade gensim

# Now showing all the model that Are Pretrained 

import gensim.downloader as api

info = api.info()
for model_name, model_data in sorted(info['models'].items()):
    num_records = model_data.get('num_records', -1)
    description = model_data.get('description', '')[:40] + '...'
    print(f'{model_name} ({num_records} records): {description}')

# Loading The Api 
wv = api.load('word2vec-google-news-300')

======You Are Ready to go to Use this model ======
