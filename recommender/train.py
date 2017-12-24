import turicreate as tc
data = tc.SFrame.read_csv('mangabox/manga_fav.csv')
data.explore()
train, test = tc.recommender.util.random_split_by_user(data, 'uid', 'manga_id')


print("#### train #####")
m = tc.recommender.create(train, user_id='uid', item_id='manga_id')

print("#### eval #####")
res = m.evaluate(test)

pro = res['precision_recall_overall']
pro.print_rows(18,3)
tc.show(pro['recall'], pro['precision'], 'recall', 'precision')

m.save('recommend.model')


