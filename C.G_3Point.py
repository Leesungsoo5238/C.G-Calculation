import numpy as np

class LandingGear:
    def __init__(self, weight, arm):
        self.weight = weight  # Weight supported by the landing gear
        self.arm = arm        # Distance from the reference point (datum)

def calculate_center_of_gravity(N_gear, L_gear, R_gear):
    total_weight = N_gear.weight + L_gear.weight + R_gear.weight
    total_moment = (N_gear.weight * N_gear.arm +
                    L_gear.weight * L_gear.arm +
                    R_gear.weight * R_gear.arm)

    if total_weight == 0:
        raise ValueError("Total weight cannot be zero.") #무게가 0일경우 예외사항
    return total_moment / total_weight    # C.G = Total Moment/Total Weight

def calculate_horizontal_cg(L_gear, R_gear):
    horizontal_weight = L_gear.weight + R_gear.weight
    horizontal_moment = (L_gear.weight * -1 * L_gear.arm + R_gear.weight * R_gear.arm)
  # 메인 랜딩기어 사이 중앙을 기준으로 왼쪽이 음(-) 오른쪽이 양(+)
    return (horizontal_moment / horizontal_weight) * 100  # *100 : convert meter into centimeter


nose_gear = LandingGear(weight=20, arm=0.18)   # unit(weight: kg, arm: m)
left_gear = LandingGear(weight=35, arm=0.535)
right_gear = LandingGear(weight=32, arm=0.535)

h_left_gear = LandingGear(weight=35, arm=0.2525)  # 날개방향 무게중심 계산에 필요한 변수
h_right_gear = LandingGear(weight=32, arm=0.2525)
# Calculate the center of gravity
mCG_aircraft = calculate_center_of_gravity(nose_gear, left_gear, right_gear)
Horizontal_aircraft = calculate_horizontal_cg(h_left_gear, h_right_gear)
print(f"Aircraft C.G is located at {mCG_aircraft:.2f} meter from the datum.")
print(f"Horizontal C.G is located at {Horizontal_aircraft:.4f} centimeter from the datum.")