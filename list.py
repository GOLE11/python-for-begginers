#LIST waa collection,ordered,changeable,and duplicate
#waxaa lagu dari karaa list-ga data types kale 
#wuxuu leeyahay index iyo negative index (index 0,1,2,3,4) negativeindex(-1,-2,-3,-4)

#Slicing waa jarjarida list-ga iyo qaar inaad sooqaadato
#example
#marka aan ranbno inaan slicing ku sameyno midka ugu sanbeeya waa inaan sidan sameynaa
#fruit = ["apple","kiwi","banana","melon","tomato"]
#print(fruit[-1]) markan waxaan isticmaalnay negativeindex

#hadii aad rabto inaad iska reebtid kan udanbeeya waxaad sameysaa sidan
#print(fruit[:-1])

#  hadii aad rabto inaad in dhexda kujirta oo list-ga mida lasoobaxdo sidan samee
#print(fruit[2:5])

#hadii aad rabto inaad gadaal kasoobilowdo jarjaridda sidan samee
#print(fruit[-4:-1])


#marka wax list-ga kamid ah aad bedelayso
#fruit = ["apple","kiwi","banana","melon","tomato"]
#fruit[1] = "gabage"
#print(fruit)
#booskii kiwi waxaa galay gabage

#LOOPING waa in list-gii lais hoos taxo
#fruit = ["apple","kiwi","banana","melon","tomato"]
#for x in fruit:
    #print(x)
#hadii aad rabto adoo is hoos dhigaya inaad midwalba index kiisa soosaarto sidan samee
#for index,x in enumerate(fruit):
    #print(index,x)

#marka aan eegayno in item-kan uu kujiro list-ga
#fruit = ["apple","kiwi","banana","melon","tomato"]
#if "banana" in fruit:
    #print("yes,banana is in list")

#else:
        #print("No!")

#marka aad rabto inaad ogaato dhererka list-ga
#print(len(fruit))

#SIDEE WAX LOOGU DARAA LIST
#1-append
#fruit = ["apple","kiwi","banana","melon","tomato"]
#fruit.append("cucumber")
#print(fruit)

#2-insert
#fruit.insert(0,"lemon")
#print(fruit)

#hadii aad rabto mid list-gs kamida indexkiisa sidan samee
#fruit = ["apple","kiwi","banana","melon","tomato"]
#print(fruit.index("melon"))

#Marka aad rabto list-ga inaad midkale kudhex darto
#fruit = ["apple","kiwi","banana","melon","tomato"]
#fruit2 = ["coconut","mango"]
#fruit.insert(0,fruit2)
#print(fruit)
#wuxuu iskudaray ayadoo labada list ay calaamadi udhaxayso
#hadaad rabto in aan waxba udhaxayn sidan samee
#Extend
#fruit.extend(fruit2)
#print(fruit)
#for shortcut waxad samayn kartaa sidan
#print(fruit+fruit2)


#SIDEE WAX UGA SAARI KARTAA LIST-GA
#fruit = ["apple","kiwi","banana","melon","tomato"]
#fruit.remove("apple")
#print(fruit)
#fruit.pop()
#print(fruit)
#waxaa baxay itemka udanbeeya listga

#MARKA AAD RABTO INAAD LIST-GA GADAAL KASOOBILOWDO "REVERSE"
#fruit = ["apple","kiwi","banana","melon","tomato"]
#fruit.reverse()
#print(fruit)
#Sorting with reverse ama kala horeysiin adoo gadaal kasoobilaabaya
#fruit.sort(reverse=True)
#print(fruit)


#KALA HOREYSIINTA AMA "SORTING ALPHABETICALLY"
#fruit = ["apple","kiwi","banana","melon","tomato"]
#fruit.sort()
#print(fruit)

#Sorting numbers lambarada kala horeysiintooda
#nums = [1,3,4,2,6,5,7]
#nums.sort()
#print(nums)
#kala horeysiin adoo dib kasoobilaabaya
#nums.sort(reverse=True)
#print(nums)

#Hadii list lagu siiyo isku dhexyaacsan aad rabto inaad isku hagaajiso sidan samee 
#nums = [1,3,4,2,6,5,7]
#sortedNumber = sorted(nums)
#print(sortedNumber)


#MAX,MIN,SUM numberka ugu badan kan ugu yar iyo wadatrooda.
#nums = [1,2,3,4,5,6,7]
#print(max(nums))
#print(min(nums))
#print(sum(nums))

#Sidee list looga dhigaa string
#fruit = ["apple","kiwi","banana","melon","tomato"]
#fruit_str = ",".join(fruit)
#print(fruit_str)

#marka aad rabto list-gii aad string kadhigtay inaad list-giisi hore kuceliso sidan samee

#fruit_list = fruit_str.split(",")
#print(fruit_list)


