from django.core.cache import cache
import pickle

tokenizer_cache_key = 'vocab_cache'
# this key is used to `set` and `get` your trained model from the cache

tokenizer = cache.get(tokenizer_cache_key)

if tokenizer is None:
    # your model isn't in the cache
    # so `set` it
    # load the pickle file
    tokenizer = pickle.load(open('polls/video_classification-tokenizer.pkl', 'rb'))
    cache.set(tokenizer_cache_key, tokenizer, None)
