revenue = int(input('Please enter a revenue amount:'))
costs = int(input('Please enter a costs amount:'))

if revenue > costs:
    roi = 100*(revenue-costs)/revenue
    print("Congratulations! You're working with profit and ROI = ", round(roi, 2),"%")
    staff = int(input('Please enter the staff quantity:'))
    print("ROI per emploee is", round(roi/staff, 2))
else:
    print("Damn, bro! There is no profit... Stop to doing that")

