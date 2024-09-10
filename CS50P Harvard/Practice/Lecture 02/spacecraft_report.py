def main():
    spacecraft = {"name" : "James Webb Space Telescope"}
    spacecraft.update({"distance" : 0.01, "orbit" : "Sun"})
    spacecraft["weight"] = 300
    print(spacecraft_report(spacecraft))

def spacecraft_report(spacecraft):
    return f'''
    =============== REPORT ===============

    Name: {spacecraft.get("name", "no input")}
    Distance: {spacecraft.get("distance", "no input")} AU
    Weight: {spacecraft.get("weight", "no input")} KG 
    Orbit: {spacecraft.get("orbit", "no input")}
    
    ======================================
'''

main()