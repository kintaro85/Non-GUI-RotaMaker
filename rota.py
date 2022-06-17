import os





class Shift():
    def __init__(self, name, letter):
        self.name = name
        #self.shiftname = [""]
        self.letter = letter


class Day():
    def __init__(self, name,mc,lc,bc,dc):
        self.name = name
        #self.monday = {:}
        #self.

        self.shift_list = []
        self.assigned_shift_list = []
        self.staff_list = []
        self.morning = 0
        self.morning_cap = mc
        self.lunch = 0
        self.lunch_cap = lc
        self.back = 0
        self.back_cap = bc
        self.dinner = 0
        self.dinner_cap = dc

        self.tenfive_cap = 0
       
        self.split = Shift("split", ["m","l","d"])
        self.ten_fiv = Shift("10-5", ["m","l","b"])
        self.tre_finish = Shift("3-f", ["b","d"])
        self.twel_elev = Shift("12-11", ["l","b","d"])
        self.five_f = Shift("5-f", ["d"])

        self.all_shift = [self.ten_fiv,self.ten_fiv,self.ten_fiv,self.split,self.tre_finish,self.twel_elev,self.five_f,self.split,self.ten_fiv,self.tre_finish,self.twel_elev,self.five_f,
        self.split,self.ten_fiv,self.tre_finish,self.twel_elev,self.five_f,self.split,self.ten_fiv,self.tre_finish,self.twel_elev,self.five_f,
        self.split,self.ten_fiv,self.tre_finish,self.twel_elev,self.five_f,self.split,self.ten_fiv,self.tre_finish,self.twel_elev,self.five_f,
        self.split,self.ten_fiv,self.tre_finish,self.twel_elev,self.five_f,self.split,self.ten_fiv,self.tre_finish,self.twel_elev,self.five_f,
        self.split,self.ten_fiv,self.tre_finish,self.twel_elev,self.five_f,self.split,self.ten_fiv,self.tre_finish,self.twel_elev,self.five_f,
        self.split,self.ten_fiv,self.tre_finish,self.twel_elev,self.five_f,self.split,self.ten_fiv,self.tre_finish,self.twel_elev,self.five_f
        ]
        
        self.is_filling = True

    def fill_x(self):
        allshift = []
        #self.morning = len(allshift)
        m = 0
        l = 0
        b = 0
        d = 0
        tenfive_counter = 0

        if self.name == "saturday":
        
            self.tenfive_cap = 1
        elif self.name == "friday":
        
            self.tenfive_cap = 1
        else:
            self.tenfive_cap = 3
        

        for shift in self.all_shift:    # add the morning
            
            if "m" in shift.letter:
                if m < self.morning_cap:
                    
                    allshift.append(shift)
                    m += 1
                    if shift == self.ten_fiv:
                        tenfive_counter += 1
                        if tenfive_counter == self.tenfive_cap:
                            for shiv in self.all_shift:
                                if shiv == self.ten_fiv:
                                    self.all_shift.remove(shiv)

                    
                    
                else:
                    for shift in self.all_shift:          # remove morning shift option
                        if "m" in shift.letter:
                            self.all_shift.remove(shift)
        
        
        for sh in allshift:            # update the lunch cap
            for letter in sh.letter:
                if letter == "l":
                    l += 1
        for shift in self.all_shift:     # add the lunch
            
            if "l" in shift.letter:
                if l < self.lunch_cap:
                    
                    allshift.append(shift)
                    l += 1
                else:
                    for shift in self.all_shift:          # remove the lunch shift option
                        if "l" in shift.letter:
                            self.all_shift.remove(shift)
        
        for sh in allshift:
            for letter in sh.letter:     # update the back cap
                if letter == "b":
                    b += 1
        for shift in self.all_shift:     # add the back
            
            if "b" in shift.letter:
                if b < self.back_cap:
                    
                    allshift.append(shift)
                    b += 1
                else:
                    for shift in self.all_shift:          # remove the back shift option
                        if "b" in shift.letter:
                            self.all_shift.remove(shift)      
        
        for sh in allshift:
            for letter in sh.letter:     # update the dinner cap
                if letter == "d":
                    d += 1
        for shift in self.all_shift:     # add the back
            
            if "d" in shift.letter:
                if d < self.dinner_cap:
                    
                    allshift.append(shift)
                    d += 1
                else:
                    for shift in self.all_shift:          # remove the back shift option
                        if "d" in shift.letter:
                            self.all_shift.remove(shift)
        
        #self.assigned_shift_list = allshift
        for shift in allshift:
            self.assigned_shift_list.append(shift.name)

        print(self.name)
        for shift in self.assigned_shift_list:
                      
            print(shift)
        print()
        
        
        print(m)
        print(l)
        print(b)
        print(d)
        print()


           
    

class StaffName():
    def __init__(self, name, dayyes, shift_can_do,tenfiv_counter,split_counter,twelel_counter,trefin_counter,special):
        self.name = name
        self.dayyes = dayyes
        self.shift_can_do = shift_can_do
        self.tenfiv_counter = tenfiv_counter
        self.split_counter = split_counter
        self.twelel_counter = twelel_counter
        self.trefin_counter = trefin_counter
        self.special = special
        
        self.day_shift_counter = 1
        self.overall_couter = 5

        self.shift_in_day = 1
        self.shift_in_week = 5

        self.day_shiftcounter = 0
        self.week_counter = 0
        
        self.shift_assigned = []
        self.hours_assigned = 0

        self.can_do_more = True

        self.max_shift = 5

        self.sat_cun = 0
        self.sat_max = 1

        self.tue_cun = 0
        self.tue_max = 1

        self.wed_cun = 0
        self.wed_max = 1

        self.thu_cun = 0
        self.thu_max = 1

        self.fri_cun = 0
        self.fri_max = 1

        self.unwanted_shift = []

        self.split = Shift("split", ["m","l","d"])
        self.ten_fiv = Shift("10-5", ["m","l","b"])
        self.tre_finish = Shift("3-f", ["b","d"])
        self.twel_elev = Shift("12-11", ["l","b","d"])
        self.five_f = Shift("5-f", ["d"])
        #self.yes = yes
        #self.no = no
        #self.monday = {"shift":"staffname"}



class Rota():
    def __init__(self):
        
        #self.shiftname = [""]
        
        self.saturday = Day("saturday",3,7,6,14)
        self.tuesday = Day("tuesday",4,5,4,8)
        self.wednesday = Day("wednesday",3,5,4,8)
        self.thursday = Day("thursday",3,5,4,8)
        self.friday = Day("friday",3,6,4,9)
        
        self.all_days = [self.saturday,self.tuesday,self.wednesday,self.thursday,self.friday]
        
        self.jen = StaffName("jen", ["tuesday","wednesday","thursday","friday","saturday"],["10-5"],5,0,0,0,[])
        self.fede = StaffName("fede", ["tuesday","wednesday","thursday","friday","saturday"],["split","10-5","3-f","12-11","5-f"],1,1,2,1,[])
        self.steven = StaffName("steven",["tuesday","wednesday","thursday","friday","saturday"],["10-5","3-f","12-11","5-f"],1,0,3,1,[])
        self.matt = StaffName("matt",["tuesday","wednesday","thursday","friday","saturday"],["split","10-5","3-f","12-11","5-f"],1,1,2,1,[])
        self.annie = StaffName("annie",["tuesday","wednesday","thursday","friday","saturday"],["split","3-f","12-11","5-f"],1,1,2,1,["wednesday","10-5"])
        self.shish = StaffName("shish",["tuesday","wednesday","thursday","friday","saturday"],["split","10-5","3-f","12-11","5-f"],1,1,2,1,[])
        #self.shish = StaffName("shish",["monday","tuesday","wednesday","thursday","friday","saturday"],["split","10-5","3-f","12-11","5-f"],1,1)
        
        self.bob = StaffName("bob",["monday","tuesday","wednesday","thursday","friday","saturday"],["split","10-5","3-f","12-11","5-f"],1,1,2,3,[])
        self.james = StaffName("james",["tuesday","wednesday","thursday","friday","saturday"],["split","10-5","3-f","12-11","5-f"],1,1,2,3,[])

        self.beth = StaffName("beth",["tuesday","thursday","saturday"],["5-f"],1,1,2,3,["tuesday","12-11"])
        self.karolina = StaffName("karolina",["tuesday","wednesday","thursday","friday","saturday"],["5-f"],1,1,2,3,["saturday","split","3-f","12-11","5-f"])
        self.celine = StaffName("celine",["tuesday","wednesday","thursday","friday","saturday"],["5-f"],1,1,2,3,["saturday","split","3-f","12-11","5-f"])
        
        self.maisy = StaffName("maisy",["tuesday","wednesday","thursday","friday","saturday"],["5-f"],1,1,2,3,["saturday","split","3-f","12-11","5-f"])
        self.luke = StaffName("luke",["tuesday","wednesday","thursday","friday","saturday"],["5-f"],1,1,2,3,["saturday","split","3-f","12-11","5-f"])
        self.brian = StaffName("brian",["tuesday","wednesday","thursday","friday","saturday"],["5-f"],1,1,2,3,["saturday","split","3-f","12-11","5-f"])
        self.ana = StaffName("ana",["saturday"],["5-f"],0,0,0,3,[])
        self.freya = StaffName("freya",["tuesday","wednesday","thursday","friday","saturday"],["5-f"],1,1,2,3,["saturday","split","3-f","12-11","5-f"])
        self.nafisa = StaffName("nafisa",["tuesday","wednesday","thursday","friday","saturday"],["5-f"],1,1,2,3,["saturday","split","3-f","12-11","5-f"])
        self.paul = StaffName("paul",["tuesday","wednesday","thursday","friday","saturday"],["5-f"],1,1,2,3,["saturday","split","3-f","12-11","5-f"])
        self.brooke = StaffName("brooke",["tuesday","wednesday","thursday","friday","saturday"],["5-f"],1,1,2,3,["saturday","split","3-f","12-11","5-f"])
        self.phoebe = StaffName("phoebe",["tuesday","wednesday","thursday","friday","saturday"],["5-f"],1,1,2,3,["saturday","split","3-f","12-11","5-f"])

        self.all_staff = [self.jen,self.annie,self.fede,self.steven,self.matt,self.shish,self.bob,self.james,self.beth,self.karolina,self.celine,
        self.maisy,self.luke,self.brian,self.ana,self.freya,self.nafisa,self.paul,self.brooke,self.phoebe]
        #self.fede,self.cheryl,self.james,self.bob,self.steven,self.shish,self.annie,self.matt,self.chris,self.george,
        #self.fede,self.cheryl,self.james,self.bob,self.steven,self.shish,self.annie,self.matt,self.chris,self.george,
        #self.fede,self.cheryl,self.james,self.bob,self.steven,self.shish,self.annie,self.matt,self.chris,self.george,
        #self.fede,self.cheryl,self.james,self.bob,self.steven,self.shish,self.annie,self.matt,self.chris,self.george]

        self.rota_ready = False

    def check_special_shift(self):
        for staf in self.all_staff:
            for shift in staf.shift_assigned:
                if shift == "split":
                    pass
                    #print("HOOOOOOOOOOOOOOOOO")
                    #staf.shift_can_do.remove("split")
                #elif shift == "10-5":
                    #staf.shift_can_do.remove(shift)

    
    def boh(self):
        for day in self.all_days:
            day.fill_x()
        
        
                   
        for staf in self.all_staff:
            #if staf.sat_cun < staf.sat_max:
            for shit in self.saturday.assigned_shift_list:
                if staf.sat_cun < staf.sat_max:
                    staf.shift_assigned.append(self.saturday.name)
                    staf.shift_assigned.append(shit)
                    self.saturday.assigned_shift_list.remove(shit)
                    #if shit == "split":
                        #staf.unwanted_shift.append(shit)
                    #if shit == "10-5":
                        #staf.unwanted_shift.append(shit)


                    staf.sat_cun += 1
        
        #self.check_special_shift()
        for staf in self.all_staff:
            #if staf.sat_cun < staf.sat_max:
            for shit in self.tuesday.assigned_shift_list:
                if staf.tue_cun < staf.tue_max:
                    if shit in staf.shift_assigned:
                        pass
                    else:
                        staf.shift_assigned.append(self.tuesday.name)
                        staf.shift_assigned.append(shit)
                        self.tuesday.assigned_shift_list.remove(shit)
                        

                        staf.tue_cun += 1
        
        #self.check_special_shift()
        for staf in self.all_staff:
            #if staf.sat_cun < staf.sat_max:
            for shift in self.wednesday.assigned_shift_list:
                if staf.wed_cun < staf.wed_max:
                    if shit in staf.shift_assigned:
                        pass
                    else:
                    
                        staf.shift_assigned.append(self.wednesday.name)
                        staf.shift_assigned.append(shift)
                        self.wednesday.assigned_shift_list.remove(shift)
                            

                        staf.wed_cun += 1

        #self.check_special_shift()
        for staf in self.all_staff:
            #if staf.sat_cun < staf.sat_max:
            for shift in self.thursday.assigned_shift_list:
                if staf.thu_cun < staf.thu_max:
                    if shit in staf.shift_assigned:
                        pass
                    else:
                        staf.shift_assigned.append(self.thursday.name)
                        staf.shift_assigned.append(shift)
                        self.thursday.assigned_shift_list.remove(shift)
                            

                        staf.thu_cun += 1

        #self.check_special_shift()
        for staf in self.all_staff:
            #if staf.sat_cun < staf.sat_max:
            for shift in self.friday.assigned_shift_list:
                if staf.fri_cun < staf.fri_max:
                    if shit in staf.shift_assigned:
                        pass
                    else:
                        staf.shift_assigned.append(self.friday.name)
                        staf.shift_assigned.append(shift)
                        self.friday.assigned_shift_list.remove(shift)
                        

                        staf.fri_cun += 1
        
        #for day in self.all_days:
            #print

        for staf in self.all_staff:
            print(staf.name)
            print(staf.shift_assigned)


    #def create_week(self):
      #  self.cr
    def create_new_week(self):
        saturday_shift = self.saturday.assigned_shift_list
        tuesday_shift =  self.tuesday.assigned_shift_list
        #self.create_staff_rota(self.fede,)

    def create_staff_rota(self, name,shift):
        pass
        """ staf_dic = {}
        for key in self.all_days:
            for value in :
                staf_dic[key] = value """

    
    def create_days_dic(self,day):
        day.fill_x()

        #utimate_dic = {}
        
        staf_can_split = []
        staf_can_tenfiv = []
        staf_can_twelelev = []
        staf_can_trefin = []
        staf_can_fivfin = []

        all_split = []
        all_tenfiv = []
        all_trefin = []
        all_twelelev = []
        all_fivfin = []
 
        for shift in day.assigned_shift_list:
            # here devide all the shift that need covering in 5 list
            if shift == "split":
                all_split.append(shift)
            elif shift == "10-5":
                all_tenfiv.append(shift)
            elif shift == "3-f":
                all_trefin.append(shift)
            elif shift == "12-11":
                
                all_twelelev.append(shift)
            else:
                all_fivfin.append(shift)
        
        
        # here devide all availeble staf that day in 5 list     
        for staf in self.all_staff:
            if len(staf_can_tenfiv) < len(all_tenfiv):
                if day.name in staf.dayyes:
                    if "10-5" in staf.shift_can_do:
                        if staf.tenfiv_counter > 0:
                            if staf.day_shift_counter > 0:
                                if staf.overall_couter > 0:
                                    staf_can_tenfiv.append(staf.name)
                                    staf.day_shift_counter -= 1
                                    staf.overall_couter -= 1
                                    staf.tenfiv_counter -= 1
                                    staf.shift_assigned.append(day.name)
                                    staf.shift_assigned.append("10-5")
                                    staf.hours_assigned += 6.5
                    if "10-5" in staf.special:
                        if day.name in staf.special:
                            if staf.tenfiv_counter > 0:
                                if staf.day_shift_counter > 0:
                                    if staf.overall_couter > 0:
                                        staf_can_tenfiv.append(staf.name)
                                        staf.day_shift_counter -= 1
                                        staf.overall_couter -= 1
                                        staf.tenfiv_counter -= 1
                                        staf.shift_assigned.append(day.name)
                                        staf.shift_assigned.append("10-5")
                                        staf.hours_assigned += 6.5
        
        
        
        
        
        
        for staf in self.all_staff:
            if len(staf_can_split) < len(all_split):
                if day.name in staf.dayyes:
                    if "split" in staf.shift_can_do:
                        if staf.split_counter > 0:
                            if staf.day_shift_counter > 0:
                                if staf.overall_couter > 0:
                                #staf.shift_counter -= 1
                                    staf_can_split.append(staf.name)
                                    staf.day_shift_counter -= 1
                                    staf.overall_couter -= 1
                                    staf.split_counter -= 1
                                    staf.shift_assigned.append(day.name)
                                    staf.shift_assigned.append("split")
                                    staf.hours_assigned += 10
                    if "split" in staf.special:
                        if day.name in staf.special:
                            if staf.split_counter > 0:
                                if staf.day_shift_counter > 0:
                                    if staf.overall_couter > 0:
                                    #staf.shift_counter -= 1
                                        staf_can_split.append(staf.name)
                                        staf.day_shift_counter -= 1
                                        staf.overall_couter -= 1
                                        staf.split_counter -= 1
                                        staf.shift_assigned.append(day.name)
                                        staf.shift_assigned.append("split")
                                        staf.hours_assigned += 10
        
        
            
        
        for staf in self.all_staff:
            if len(staf_can_twelelev) < len(all_twelelev):
                if day.name in staf.dayyes:
                    if "12-11" in staf.shift_can_do:
                        if staf.twelel_counter > 0:
                            if staf.day_shift_counter > 0:
                                if staf.overall_couter > 0:    
                                    staf_can_twelelev.append(staf.name)
                                    staf.day_shift_counter -= 1
                                    staf.overall_couter -= 1
                                    staf.twelel_counter -= 1
                                    staf.shift_assigned.append(day.name)
                                    staf.shift_assigned.append("12-11")
                                    staf.hours_assigned += 11
                    if "12-11" in staf.special:
                        if day.name in staf.special:
                            if staf.twelel_counter > 0:
                                if staf.day_shift_counter > 0:
                                    if staf.overall_couter > 0:    
                                        staf_can_twelelev.append(staf.name)
                                        staf.day_shift_counter -= 1
                                        staf.overall_couter -= 1
                                        staf.twelel_counter -= 1
                                        staf.shift_assigned.append(day.name)
                                        staf.shift_assigned.append("12-11")
                                        staf.hours_assigned += 11
                    
    
        
        for staf in self.all_staff:
            if len(staf_can_trefin) < len(all_trefin):
                if day.name in staf.dayyes:
                    if "3-f" in staf.shift_can_do:
                        if staf.trefin_counter > 0:
                            if staf.day_shift_counter > 0:
                                if staf.overall_couter > 0:      
                            
                                    staf_can_trefin.append(staf.name)
                                    staf.day_shift_counter -= 1
                                    staf.overall_couter -= 1
                                    staf.trefin_counter -= 1
                                    staf.shift_assigned.append(day.name)
                                    staf.shift_assigned.append("3-f")
                                    staf.hours_assigned += 9
                    if "3-f" in staf.special:
                        if day.name in staf.special:
                            if staf.trefin_counter > 0:
                                if staf.day_shift_counter > 0:
                                    if staf.overall_couter > 0:      
                                
                                        staf_can_trefin.append(staf.name)
                                        staf.day_shift_counter -= 1
                                        staf.overall_couter -= 1
                                        staf.trefin_counter -= 1
                                        staf.shift_assigned.append(day.name)
                                        staf.shift_assigned.append("3-f")
                                        staf.hours_assigned += 9
        
        
        for staf in self.all_staff:
            if len(staf_can_fivfin) < len(all_fivfin):
                if day.name in staf.dayyes:
                    if "5-f" in staf.shift_can_do:
                        if staf.day_shift_counter > 0: 
                            if staf.overall_couter > 0: 
                                staf_can_fivfin.append(staf.name)
                                staf.day_shift_counter -= 1
                                staf.overall_couter -= 1
                                staf.shift_assigned.append(day.name)
                                staf.shift_assigned.append("5-f")
                                staf.hours_assigned += 7
            
        
        zipped_spl = zip(staf_can_split, all_split)
        zipped_ten = zip(staf_can_tenfiv, all_tenfiv)
        zipped_twe = zip(staf_can_twelelev, all_twelelev)
        zipped_tre = zip(staf_can_trefin, all_trefin)
        zipped_fiv = zip(staf_can_fivfin, all_fivfin)
        
        diccoS = dict(zipped_spl)
        diccoTE = dict(zipped_ten)
        diccoTW = dict(zipped_twe)
        diccoTR = dict(zipped_tre)
        diccoF = dict(zipped_fiv)

        for staf in self.all_staff:
            staf.day_shift_counter +=1
        
    
        dayNshif = [diccoTE,diccoS,diccoTW,diccoTR,diccoF]
        #print(ultimate_dic)
        print(day.name)
        print(dayNshif)
        print()
        
    
    
    
    def create_week(self):
        #for day in self.all_days:
            #day.fill_x()
            
        self.create_days_dic(self.saturday)
        self.create_days_dic(self.tuesday)
        self.create_days_dic(self.wednesday)
        self.create_days_dic(self.thursday)
        self.create_days_dic(self.friday)
        
        for staf in self.all_staff:
            print(staf.name)
            
            print(staf.shift_assigned)
            print(staf.hours_assigned)
        
        if os.path.isfile('shift.txt'):
            writefile = open('shift.txt','a')
        else:
            writefile = open('shift.txt','w')

        for staf in self.all_staff:

            
            writefile.write("\n"+ str(staf.name) + " " + str(staf.shift_assigned))
        


    def create_dic(self):
        staff_names = []
        for staf in self.all_staff:
            staff_names.append(staf.name)
        for day in self.all_days:

            day.fill_x()
        dic = {}
        for key in self.tuesday.assigned_shift_list:
            for value in staff_names:
                dic[key] = value

        print(dic)

    def create_day_dic(self, day, allstaff):
        day.fill_x()

        #utimate_dic = {}
        
        staf_can_split = []
        staf_can_tenfiv = []
        staf_can_twelelev = []
        staf_can_trefin = []
        staf_can_fivfin = []

        all_split = []
        all_tenfiv = []
        all_trefin = []
        all_twelelev = []
        all_fivfin = []
 
        for shift in day.assigned_shift_list:
            # here devide all the shift that need covering in 5 list
            if shift == "split":
                all_split.append(shift)
            elif shift == "10-5":
                all_tenfiv.append(shift)
            elif shift == "3-f":
                all_trefin.append(shift)
            elif shift == "12-11":
                if "12-11" in all_twelelev:
                    all_twelelev.append(shift+"b")
                else:
                    all_twelelev.append(shift)
            else:
                all_fivfin.append(shift)
        
        
        # here devide all availeble staf that day in 5 list     
        for staf in allstaff:
            if len(staf_can_split) < len(all_split):
                if "split" in staf.shift_can_do:
                    if staf.split_counter > 0:
                        if staf.day_shift_counter > 0:
                            if staf.overall_couter > 0:
                            #staf.shift_counter -= 1
                                staf_can_split.append(staf.name)
                                staf.day_shift_counter -= 1
                                staf.overall_couter -= 1
        
        
        for staf in allstaff:
            if len(staf_can_tenfiv) < len(all_tenfiv):
                if "10-5" in staf.shift_can_do:
                    if staf.tenfiv_counter > 0:
                        if staf.day_shift_counter > 0:
                            if staf.overall_couter > 0:
                                staf_can_tenfiv.append(staf.name)
                                staf.day_shift_counter -= 1
                                staf.overall_couter -= 1
            
        
        for staf in allstaff:
            if len(staf_can_twelelev) < len(all_twelelev):
                if "12-11" in staf.shift_can_do:
                    if staf.day_shift_counter > 0:
                        if staf.overall_couter > 0:    
                            staf_can_twelelev.append(staf.name)
                            staf.day_shift_counter -= 1
                            staf.overall_couter -= 1
        
        
        for staf in allstaff:
            if len(staf_can_trefin) < len(all_trefin):
                if "3-f" in staf.shift_can_do:
                    if staf.day_shift_counter > 0:
                        if staf.overall_couter > 0:      
                    
                            staf_can_trefin.append(staf.name)
                            staf.day_shift_counter -= 1
                            staf.overall_couter -= 1
        
        
        for staf in allstaff:
            if len(staf_can_fivfin) < len(all_fivfin):
                if "5-f" in staf.shift_can_do:
                    if staf.day_shift_counter > 0: 
                        if staf.overall_couter > 0: 
                            staf_can_fivfin.append(staf.name)
                            staf.day_shift_counter -= 1
                            staf.overall_couter -= 1
            
        #ultimate_dic = {}
        #for key in all_split:
            #for value in staf_can_split:
                #ultimate_dic[key] = value
        #for key in all_tenfiv:
            #for value in staf_can_tenfiv:
                #ultimate_dic[key] = value
        
        #for key in all_twelelev:
            #for value in staf_can_twelelev:
                #ultimate_dic[key] = value
        zipped_spl = zip(all_split, staf_can_split)
        zipped_ten = zip(all_tenfiv, staf_can_tenfiv)
        zipped_twe = zip(all_twelelev, staf_can_twelelev)
        zipped_tre = zip(all_trefin, staf_can_trefin)
        zipped_fiv = zip(all_fivfin, staf_can_fivfin)
        
        diccoS = dict(zipped_spl)
        diccoTE = dict(zipped_ten)
        diccoTW = dict(zipped_twe)
        diccoTR = dict(zipped_tre)
        diccoF = dict(zipped_fiv)
                
        #for key in all_trefin:
            #for value in staf_can_trefin:
                #ultimate_dic[key] = value
        #for key in all_fivfin:
            #for value in staf_can_fivfin:
                #ultimate_dic[key] = value

        dayNshif = [diccoTE,diccoS,diccoTW,diccoTR,diccoF]
        #print(ultimate_dic)
        print(day.name)
        print(dayNshif)
        print()
            # here devide all availeble staf that day in 5 list 
        #print(all_split)
        #print(all_tenfiv)
        #print(all_twelelev)
        #print(all_trefin)
        #print(all_fivfin)

        #print()

        #print(staf_can_split)
        #print(staf_can_tenfiv)
        #print(staf_can_twelelev)
        #print(staf_can_trefin)
        #print(staf_can_fivfin)


    def view_all_week_shift(self):
        for day in self.all_days:
            day.fill_x()
            print(day.name + ":")
            for shift in day.assigned_shift_list:
                print(shift)
            print()
                


newrota = Rota()
#newrota.tuesday.fill_x()

#newrota.view_all_week_shift()    this works
#newrota.create_dic()             this not exactly as intended

#newrota.create_day_dic(newrota.saturday,newrota.all_staff)
#newrota.create_day_dic(newrota.tuesday,newrota.all_staff)
#newrota.create_day_dic(newrota.wednesday,newrota.all_staff)
#newrota.create_day_dic(newrota.thursday,newrota.all_staff)
#newrota.create_day_dic(newrota.friday,newrota.all_staff)

#newrota.create_week()

#newrota.boh()

newrota.create_week()

print("poo")







