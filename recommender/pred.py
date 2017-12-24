import turicreate as tc
m = tc.load_model('recommend.model')
manga = tc.SFrame.read_csv('mangabox/manga_id-title.csv')

print("==== input ====")
data = tc.SFrame({
    'uid': ["xxxxxx","xxxxxx","xxxxxx"],
    'manga_id': [56124,58191,40184]
    })
print(data.join(manga, on='manga_id'))

print("==== recommend ====")
res = m.recommend(['xxxxxx'], new_observation_data=data)
print(res.join(manga, on='manga_id').sort('rank'))

print(m.recommend(['zzzzzz']).join(manga, on='manga_id').sort('rank'))

print("==== similar ====")
sim_src = tc.SFrame({'manga_id': [47415]})
print(sim_src.join(manga, on='manga_id'))
print(m.get_similar_items(sim_src['manga_id']).join(manga, on={'similar':'manga_id'}).sort('score', ascending = False))

print("==== similar ====")
sim_src = tc.SFrame({'manga_id': [54275]})
print(sim_src.join(manga, on='manga_id'))
print(m.get_similar_items(sim_src['manga_id']).join(manga, on={'similar':'manga_id'}).sort('score', ascending = False))
