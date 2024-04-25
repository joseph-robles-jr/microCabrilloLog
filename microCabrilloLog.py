import datetime
from datetime import timezone #used for conversion to UTC


"""
In amateur radio, there are contests that happen to see how many stations you can get in contact with within a certain period. Logs are kept of what you do and will then be submitted to whomever runs the contest. 
These logs are in the form of a formatted txt file in the Cabrillo format. Many of the loggers available are slow, clunky, and often have been around for decades. 
I aimed to build a simple logger that creates these txt Cabrillo files in a terminal program in a way that will require minimal configuration and have little to no bells and whistles. 
This program was designed to create a cabrillo log file for an amateur radio contest known as the Idaho QSO Party. 
This typically includes the date and time, location, state, address, and a record of the contacts that have been made from that particular radio and many other parameters. The result I have ended up with is about 90% compatible with the standard. Some changes still need to be made to datetime but besides that, It works well. 


Example test input:

What is your callsign: K7BYI
Will you be using a spotting network? Y/N: Y
Are you located in Idaho? Y/N: Y
What is your 3 digit county identifier?: MAD
Are you part of a radio club? Y/N: Y
What is your club name (Not Club Callsign)?: BYU Idaho Amature Radio Club
Is BYU Idaho Amature Radio Club correct? Y/N: Y
What is your first name?: John
What is your street address?: 525 S Center St 
Now your City, State, and Zip in that order: Rexburg, ID 83460
What is your country?: United States
Enter Frequency in khz: 14250
Callsign of recived station: KI5TLZ
Input the recived RST report (59): 55
Input the sent RST report (59): 57
Input the 2 letter arrl section or the 3 leter county abreviation: TX  
Are you finished logging contacts? Y/N: n
Enter Frequency in khz: 14355
Callsign of recived station: K5WPH
Input the recived RST report (59): 57
Input the sent RST report (59): 49
Input the 2 letter arrl section or the 3 leter county abreviation: TX
Are you finished logging contacts? Y/N: y


_____________________________________________________________________

This will create and output file that contains the following:


START-OF-LOG: 2.0
ARRL-SECTION: ID
CALLSIGN: K7BYI
CLUB: BYU Idaho Amature Radio Club
CONTEST: ID-QSO-PARTY
CATEGORY: SINGLE-OP-ASSISTED ALL LOW SSB
OPERATORS: K7BYI
NAME: John
ADDRESS: 525 S Center St
ADDRESS: Rexburg, ID 83460
ADDRESS: United States
QSO: 14250 PH 2024-04-11 01:51:24.658186+00:00 K7BYI	 57 MAD	KI5TLZ	 55 TX
QSO: 14355 PH 2024-04-11 01:52:42.801839+00:00 K7BYI	 49 MAD	K5WPH	 57 TX
END-OF-LOG:


"""

def convert_to_utc():
    """Converts a given time to UTC and returns it"""
    dt = datetime.datetime.now(timezone.utc)


    return dt #OUTPUT MAY NEED TO BE TWEAKED T0 CONFORM TO .log


def give_me_a_bool(string_to_print): # Function complete
    """Prints a given string, then Promps user for input of a 'Y' or an 'N'. If neither, Ask again, Else, return value as True or False"""
    
    true_or_false = "blank_value" #initialize the loop
    #loop will run until the input is a Y or N. Then it coverts it to a BOOL stored in true_or_false
    while true_or_false != True and true_or_false != False:
        #prints string_to_print message, then prompts for input of a Y or N
        print(string_to_print, end = '')
        inital_input = input(" Y/N: ").upper()
        
        if inital_input == 'Y' or inital_input == 'YES': #tests input for Yes and convert true_or_false to trye
            true_or_false = True
        elif inital_input == 'N' or inital_input == 'NO':
            true_or_false = False
        else:
            print("Please try again! Input only a 'Yes' or 'No' Value.\n" )

    return true_or_false


def collect_header_info():
    
    """Collects header info the the Idaho QSO Party cabrillo file and returns a dictionary"""
    
    collected_dict = {
        "arrl-section" : "",
        "callsign" : "",
        "catagory_assisted" : "",
        "catagory_band" : "ALL",
        "club" : "",
        "name" : "",
        "address 1" : "",
        "address 2" : "",
        "city_state_zip" : "",
        "country" : "United States",
        "county or DX" : ""



    }
    
    #get the callsign of the user
    callsign = str(input("What is your callsign?: "))
    #clean up common input mistakes
    callsign.strip(" ")
    callsign.strip()
    collected_dict["callsign"] = callsign.replace("Ø", "0") #convert crossed zero to standrd 0 value
     
    #Will a spotting network be used; sets Assisted catagory
    is_assisted = give_me_a_bool("Will you be using a spotting network?") #return BOOL. Yes is true. No is False here\
    if is_assisted == True:
        catagory_assisted = "ASSISTED"
    elif is_assisted == False:
        collected_dict['catagory_assisted'] = "NON-ASSISTED"
    
    ##chacks location of the user
    idaho = give_me_a_bool("Are you located in Idaho?") #Returns BOOL
    if idaho == True:
        state = "ID"
        collected_dict["arrl-section"] = state
        county = ""
        #ask for 3 letter county ID
        while len(county) != 3:
            input_state = str(input("What is your 3 digit county identifier?: "))
            #check for length of 3 letters. Reprompt if not
            if len(input_state) == 3:
                county = input_state
                collected_dict["county or DX"] = input_state
    elif idaho == False:
        state = ""
        # ask for 2 digit state or DX
        
        while len(state) != 2:
            input_state = str(input("What is your 2 letter state ID (i.e. AZ, TX, ID etc...)? If out of USA, please enter 'DX' ").upper())

            input_arrl_section = input('What is your ARRL section?: ')
            collected_dict["arrl-section"] = input_arrl_section

            
            if len(input_state) == 2:
                state = input_state
            
        
    #What club are you a part of?
    is_part_of_club = give_me_a_bool("Are you part of a radio club?")
    if is_part_of_club == True:
        club_correct = False 

        #ensures that the user entered the correct value
        while club_correct == False:
            input_club = input("What is your club name (Not Club Callsign)?: ")
            club_check_string = (f"Is {input_club} correct?")
            club_correct = give_me_a_bool(club_check_string)
            if club_correct == True:
                club = input_club.capitalize()
                collected_dict['club'] = club
            else:
                pass
    collected_dict['name'] = input("What is your first name?: ")
    collected_dict['address 1'] = input("What is your street address?: ")
    
    collected_dict['city_state_zip'] = input("Now your City, State, and Zip in that order: ")
    collected_dict['country'] = input("What is your country?: ")




    return collected_dict
        
def print_to_log(header_dictionary):
    """Writes the header file to the log.cabrillo file in the proper format"""

    #creates log.log and appends the details from teh header_dictionary that has been passed.
    with open('log.log', 'a') as file:
        file.write("START-OF-LOG: 2.0\n")
        file.write(f"ARRL-SECTION: {header_dictionary['arrl-section']}\n")
        file.write(f"CALLSIGN: {header_dictionary['callsign']}\n")
        file.write(f"CLUB: {header_dictionary['club']}\n")
        file.write(f"CONTEST: ID-QSO-PARTY\n")
        file.write(f"CATEGORY: SINGLE-OP-ASSISTED ALL LOW SSB\n")
        file.write(f"OPERATORS: {header_dictionary['callsign']}\n")
        file.write(f"NAME: {header_dictionary['name']}\n")
        file.write(f"ADDRESS: {header_dictionary['address 1']}\n")
        file.write(f"ADDRESS: {header_dictionary['city_state_zip']}\n")
        file.write(f"ADDRESS: {header_dictionary['country']}\n")
        #endof header writing

def start_logging(header_dictionary):
    """
    Requires a dictionary of the header. 
    Writes QSO data, including RST, Calsign, and current time to the log.log file until user trminates the function.
    """
    end_logging = False
    while end_logging != True:
        with open('log.log', 'a') as file:
            file.write("QSO: ")
            current_frequency = input("Enter Frequency in khz: ")
            rx_callsign = input('Callsign of recived station: ').upper()
            rst_recived = input("Input the recived RST report (59): ")
            
            rst_sent = input("Input the sent RST report (59): ")

            exchange_recived = input('Input the 2 letter arrl section or the 3 leter county abreviation: ').upper()
            
            utc_time = convert_to_utc()
            

            file.write(f"{current_frequency} PH {utc_time} {header_dictionary['callsign']}\t {rst_sent} {header_dictionary['county or DX']}\t{rx_callsign}\t {rst_recived} {exchange_recived}\n")

            
            end_logging = give_me_a_bool("Are you finished logging contacts?")
        
        with open('log.log', 'a') as file:
            file.write("\nEND-OF-LOG:")

    print("Log complete and exported")



def main():
    """Runs the program"""
    header_dictionary = collect_header_info()
    print_to_log(header_dictionary)
    start_logging(header_dictionary)


if __name__ == "__main__":
    main()
    


