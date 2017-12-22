import turicreate as tc


data = tc.SFrame('faces.sframe')
sample = data[:10]

model = tc.load_model('mcz.model')
sample['predictions'] = model.predict(sample)

print(sample)
