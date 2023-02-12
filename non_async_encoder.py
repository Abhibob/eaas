import sys
import json
import numpy as np
from flask import Flask, request
from sentence_transformers import models, losses, SentenceTransformer
global word_embedding_model
global pooling_model
global dense_model
global transformer

word_embedding_model = models.DistilBERT('distilbert-base-uncased')
pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension(),
                              pooling_mode_mean_tokens=True,
                              pooling_mode_cls_token=False,
                              pooling_mode_max_tokens=False)
dense_model = models.Dense(in_features=768, out_features=256)
transformer = SentenceTransformer(modules=[word_embedding_model, pooling_model, dense_model])

class NumpyEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, np.ndarray):
      return obj.tolist()
    return json.JSONEncoder.default(self, obj)

app = Flask(__name__)
@app.route('/', methods=['GET'])
def texttovector():
  s = [request.args.get('text')]
  # reduce dim from 768 to 256

  sentences = s
  sentence_embeddings = transformer.encode(sentences)

  print(sentence_embeddings)
  for sentence, embedding in zip(sentences, sentence_embeddings):
   print("Sentence:", sentence)
   print("Embedding:", embedding)
  return json.dumps(sentence_embeddings, cls=NumpyEncoder)
