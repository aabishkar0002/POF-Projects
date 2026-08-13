# Project: Music Library 

# Instead of using a database,save everything in music.json.
#So basically assuming that datas are already present
# or to be kept in a json file
#---------------------------------------------------------------------
import json

file = "music_library.json"

class Music_Player:

    def add_music(self,artist_details):
       
      #to store in a valid json forma
      #load -> append -> dump
      
      with open(file,"r") as f:      
        songs = json.load(f)
      
      with open(file,"w") as thisfile:

        songs.append(artist_details)

        json.dump(songs,thisfile,indent = 2) #isnot json i.e dict

      print("Added to library...")



    def delete_music(self,an,sn):

    #songs a global varaible is still in list py obj
    #the format of ob is like list->dict,dict so not easily accessable
      with open(file,"r") as f:      
        songs = json.load(f)   

      status = False

      for lines in songs:
          
          if an == lines["artist_name"] and sn == lines["song_name"]:

              songs.remove(lines)

              with open(file,"w") as fah:
                  json.dump(songs,fah,indent = 2)
                 
              print(f"{sn} by {an} removed..")
              status = True
                          

      if status == True:
        pass

      else:          
          print("Artist/Song name doesnt match..\n")
            

    def show_library(self):

       #to show whatever in json file into terminal
       
       with open(file,"r") as fw:

          songs = json.load(fw)

          for lines in songs:
             print("Artist : ",lines["artist_name"])
             print("Song : ",lines["song_name"])
             print("Genre : ",lines["genre"])
             print("\n")
       
#---------------------------------------------------------------------


M = Music_Player() #assuming initialy before pass as empty
#----------------------------------------------------------------------
#Showing on a Terminal
i = 1 #Safe bet


while True:
# ------------------------------------------------------------------------
    print("|---------- Welcome to Music Player ----------|")

    for options in ["add music","delete music","music library"]:
        
        print(f"Enter {i} to {options}")
        i += 1

        if i == 4:
            i = 1
            break


     #---------choosing an option-----------

    select = int(input("\nEnter one of the option[numbers] above => "))
 
    match(select):

        case 1:
            artist_name = input("Enter Artist name : ")
            song_name = input("Enter Song name : ")
            genres = input("Enter genre : ")
            artist_details = {
              "artist_name":artist_name,
              "song_name" : song_name,
              "genre" : genres
            }                      
            M.add_music(artist_details)



        case 2:

          an = input("Enter artist_name to delete : ")
          sn = input("Enter song_name to delete : ")          
          M.delete_music(an,sn)


        case 3:

              M.show_library()

          
      
#--------------------------------------------------------------------------
     
     