import turicreate as tc
actions = tc.SFrame.read_csv('mangabox/comp_rate.csv')
train, test = tc.recommender.util.random_split_by_user(actions, 'uid', 'manga_id')

actions = tc.SFrame.read_csv('mangabox/comp_rate.csv')
print("#### train #####")
m = tc.recommender.create(train, user_id='uid', item_id='manga_id', target='comp_rate')

print("#### eval #####")
eval = m.evaluate(test)
print(eval)

m.save('recommend.model')


