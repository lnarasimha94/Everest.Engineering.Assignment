import itertools



def calculateCost(basecost,weight,distance):
    return basecost+(weight*10)+(distance * 5)


  
# Defining main function
def main():

    coupons  = {
    # couponcode, percent, distance, weight
    'OFR001':[10,'<200','70-200'],
    'OFR002':[7,'50-150','100-250'],
    'OFR003':[5,'50-250','10-150']
    }

    firstLine = input(" ")
    base_delivery_cost = float(firstLine.split(" ")[0])
    no_of_packges = int(firstLine.split(" ")[1])


    package_details = []
    package_details_dict= {}
    for i in range(no_of_packges):
        packageInput = input("")
        package_details.append(packageInput.split(" "))
        package_details_dict[packageInput.split(" ")[0]] = packageInput.split(" ")


    secondLine = input(" ")
    no_of_vehicles = int(secondLine.split(" ")[0])
    max_speed = int(secondLine.split(" ")[1])
    max_load = int(secondLine.split(" ")[2])



    final_Resp = {}

    print("*****************")

    package_names = []

    for package in package_details:

        package_weight = float(package[1])
        package_distance = float(package[2])
        package_name  = package[0]
        package_names.append(package_name)

        delivery_cost = calculateCost(base_delivery_cost,package_weight,package_distance)

        applied_coupon = package[3].upper()

        if applied_coupon in coupons.keys():

            coupon_details = coupons[applied_coupon]

            weight_check = False
            if('-' in coupon_details[2]):
                weight_split = coupon_details[2].split('-')
                min_weight = float(weight_split[0])
                max_weight = float(weight_split[1])
                if package_weight >= min_weight and package_weight <= max_weight:
                    weight_check = True
            elif('<' in coupon_details[2]):
                max_weight = coupon_details[2].replace('<','')
                max_weight = float(max_weight)
                if package_weight < max_weight:
                    weight_check = True
            elif('>' in coupon_details[2]):
                min_weight = coupon_details[2].replace('>','')
                min_weight = ifloatnt(min_weight)
                if package_weight > min_weight:
                    weight_check = True  
            elif float(coupon_details[2]) == package_weight:
                    weight_check = True 

            
            distance_check = False
            if('-' in coupon_details[1]):
                dist_split = coupon_details[1].split('-')
                min_distance = float(dist_split[0])
                max_distance = float(dist_split[1])
                if package_distance >= min_distance and package_distance <= max_distance:
                    distance_check = True
            elif('<' in coupon_details[1]):
                max_distance = coupon_details[1].replace('<','')
                max_distance = float(max_distance)
                if package_distance < max_distance:
                    distance_check = True
            elif('>' in coupon_details[1]):
                min_distance = coupon_details[1].replace('>','')
                min_distance = float(min_distance)
                if package_distance > min_distance:
                    distance_check = True  
            elif float(coupon_details[1]) == package_distance:
                    distance_check = True

            if(distance_check and weight_check):
                delivery_cost = delivery_cost - (delivery_cost/100)*coupon_details[0]

        #print(package[0] +":"+str(delivery_cost))
        final_Resp[package[0]]  = [package[0],coupon_details[0],delivery_cost]





    listOfLists = [0] * no_of_vehicles



    while(len(package_names) != 0):
        combinations = [combination for i in range(len(package_names)+1) for combination in itertools.combinations(package_names, i)]
        total_weights = []
        combinations_valid = []
        max_dist_each_combo  = []
        for combination in combinations:
            sum_weight = 0
            max_dist = 0
            for pkg in combination:
                sum_weight = sum_weight + int(package_details_dict[pkg][1])
                if(int(package_details_dict[pkg][1]) > max_dist):
                    max_dist = int(package_details_dict[pkg][1])
            
            if(max_weight > sum_weight):
                total_weights.append(sum_weight)
                combinations_valid.append(combination)
                max_dist_each_combo.append(max_dist)


        max_w_index = total_weights.index(max(total_weights))
        print(combinations_valid[max_w_index])

        distances_picked = []
        for i in combinations_valid[max_w_index]:
            distances_picked.append(int(package_details_dict[i][2]))
        

        time_taken_for_total_drive = (max(distances_picked)/max_speed)

        try:
            #print(time_taken_for_total_drive)
            index = listOfLists.index(0)
            listOfLists[index] = float("{:.2f}".format(time_taken_for_total_drive*2))
        except:
            index = listOfLists.index(min(listOfLists))
            listOfLists[index] = ( float("{:.2f}".format(time_taken_for_total_drive*2)) )+listOfLists[index]


        for ele in combinations_valid[max_w_index]:
            if ele in package_names:
                package_names.remove(ele)
            
        if(len(package_names) == 0):
            listOfLists[index] = listOfLists[index] -  time_taken_for_total_drive

    print("*****************")       
    print("Vehicle wise time spent on delivery :"+str(listOfLists))
  

if __name__=="__main__":
    main()







