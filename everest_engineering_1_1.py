def calculateCost(basecost,weight,distance):
    return basecost+(weight*10)+(distance * 5)



coupons  = {
    # couponcode, percent, distance, weight
    'OFR001':[10,'<200','70-200'],
    'OFR002':[7,'50-150','100-250'],
    'OFR003':[5,'50-250','10-150']
}


#sample input
# 100 3
# name, weight, distance, coupon
# pkg1 5 5 ofr001
# pkg2 15 5 ofr002
# pkg3 10 100 ofr003

firstLine = input(" ")
base_delivery_cost = float(firstLine.split(" ")[0])
no_of_packges = int(firstLine.split(" ")[1])


package_details = []
for i in range(no_of_packges):
    packageInput = input("")
    package_details.append(packageInput.split(" "))

print("*****************")

for package in package_details:

    package_weight = float(package[1])
    package_distance = float(package[2])

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
    print(package[0] +":"+str(delivery_cost))

