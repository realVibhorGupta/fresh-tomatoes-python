import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/6/69/Toy_Story_3_poster.jpg/220px-Toy_Story_3_poster.jpg",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")
 
#print (toy_story.storyline)


avatar= media.Movie("Avatar",
                        "A marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=EPTHpG7ovak")
 
#print (avatar.storyline)
#avatar.show_trailer()

tanu_weds_manu_returns=media.Movie("Tanu Weds Manu Returns",
                       "A Different LOve Story",
                       "http://media2.intoday.in/indiatoday/images/stories//2015April/tanu-mos_041515102628.jpg",
                       "https://www.youtube.com/watch?v=wGGmyaurjAI")

#print(tanu_weds_manu_returns.storyline) 

#tanu_weds_manu_returns.show_trailer()

two_states=media.Movie("2 STATES",
                 "A love story of two people from two different states  of INDIA",
                 "https://upload.wikimedia.org/wikipedia/en/thumb/1/12/2_States_poster.jpg/220px-2_States_poster.jpg",
                "https://www.youtube.com/watch?v=CGyAaR2aWcA")

singham_returns=media.Movie("SINGHAM RETURNS",
                            "An action thriller of a honest cop",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/8/83/Singham_Returns_Poster.jpg/220px-Singham_Returns_Poster.jpg",
                            "https://www.youtube.com/watch?v=3CwQjsdE-1Q")


the_shaukeens=media.Movie("The Shaukeens",
                           "Story of three Pevert old age people",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/4/42/The_Shaukeens_2.jpg/220px-The_Shaukeens_2.jpg",
                          "https://www.youtube.com/watch?v=eg4tfauEn7c")



movies=[toy_story,avatar,tanu_weds_manu_returns,two_states,singham_returns,the_shaukeens]
#fresh_tomatoes.open_movies_page(movies)

#print (media.Movie. VALID_RATINGS)

print (media.Movie.__doc__)




