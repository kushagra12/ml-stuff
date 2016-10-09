import recommendations

critics = recommendations.critics

# print(critics['Lisa Rose'])
#
# print("Similarity using Euclidean Distance: \n")
# # Using Euclidean Distance
# for critic in critics:
#     print("Similarity with " + critic + " : " + str(recommendations.sim_distance("Lisa Rose", critic, critics)))
#
# print("Similarity using Pearson Correlation: \n")
# # Using Correlation
# for critic in critics:
#     print("Similarity with " + critic + " : " + str(recommendations.sim_pearson("Lisa Rose", critic, critics)))

print("Top 5 Matches for Lisa")
print(recommendations.top_matches("Lisa Rose",critics))

print("Recommendations for Toby")
print(recommendations.get_recommendations("Toby",critics))

movies = recommendations.flip_params(critics)

print("If you like superman returns then")
print(recommendations.top_matches("Superman Returns", movies))

