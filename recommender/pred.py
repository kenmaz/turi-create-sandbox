import turicreate as tc
m = tc.load_model('recommend.model')
manga = tc.SFrame.read_csv('mangabox/manga_id-title.csv')

print("==== input ====")
data = tc.SFrame({
    'uid': ["kenmaz", "kenmaz", "kenmaz", "kenmaz"],
    'manga_id': [203, 237, 56124, 58443],
    'comp_rate': [1.0, 1.0, 0.1, 0.1]
    })
print(data.join(manga, on='manga_id').sort('comp_rate', ascending = False))

print("==== recommend ====")
res = m.recommend(['kenmaz'], new_observation_data=data)
print(res.join(manga, on='manga_id').sort('rank'))

print(m.recommend(['new_user']).join(manga, on='manga_id').sort('rank'))

print("==== similar ====")
sim_src = tc.SFrame({'manga_id': [59579]})
print(sim_src.join(manga, on='manga_id'))
print(m.get_similar_items(sim_src['manga_id']).join(manga, on={'similar':'manga_id'}).sort('score', ascending = False))


m.export_coreml('MangaRecommender.mlmodel')
