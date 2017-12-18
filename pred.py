import turicreate as tc
m = tc.load_model('recommend.model')
manga = tc.SFrame.read_csv('mangabox/manga_id-title.csv')

print("==== input ====")
data = tc.SFrame({
    'uid': ["kenmaz", "kenmaz", "kenmaz"],
    'manga_id': [203, 237, 56124],
    'comp_rate': [1.0, 1.0, 0.1]
    })
print(data.join(manga, on='manga_id').sort('comp_rate', ascending = False))

print("==== recommend ====")
res = m.recommend(['kenmaz'], new_observation_data=data)
print(res.join(manga, on='manga_id').sort('rank'))
