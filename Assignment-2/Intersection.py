#
# Complete the 'find_intersections' function below.
#

def find_intersections(c_x, c_y, c_z, c_r,
                       ray_x, ray_y, ray_z, dir_x, dir_y, dir_z):
    """
    Args:
        c_x, c_y, c_z (float): coordinates of center point of the sphere.
        c_r (float): radius of the sphere.
        ray_x, ray_y, ray_z (float): coordinates of the origin of the ray.
        dir_x, dir_y, dir_z (float): direction vector of the ray.

    Returns:
        [] or list of floats

    """
    # Write your code here
    #     equation_circle = (x-c_x)**2 + (y-c_y)**2 + (z-c_z)**2 == (c_r)**2
    #     x=ray_x + dir_x*t
    #     y=ray_y + dir_y*t
    #     z=ray_z + dir_z*t
    a = dir_x ** 2 + dir_y ** 2 + dir_z ** 2
    b = 2 * (dir_x * (ray_x - c_x) + dir_y * (ray_y - c_y) + dir_z * (ray_z - c_z))
    c = c_x ** 2 + c_y ** 2 + c_z ** 2 + ray_x ** 2 + ray_y ** 2 + ray_z ** 2 - 2 * (
            c_x * ray_x + c_y * ray_y + c_z * ray_z) - c_r ** 2

    d = b ** 2 - 4 * a * c
    returnList = []
    if d < 0:
        return returnList.append(float(0))
    elif d == 0:
        t = -b / (2 * a)
        return returnList.append(distance(ray_x + dir_x * t, ray_y + dir_y * t, ray_z + dir_z * t, ray_x, ray_y, ray_z))
    else:
        t1 = (-b + d ** 0.5) / (2 * a)
        t2 = (-b - d ** 0.5) / (2 * a)
        dist1 = distance(ray_x + dir_x * t1, ray_y + dir_y * t1, ray_z + dir_z * t1, ray_x, ray_y, ray_z)
        dist2 = distance(ray_x + dir_x * t2, ray_y + dir_y * t2, ray_z + dir_z * t2, ray_x, ray_y, ray_z)
        returnList.append(dist1)
        returnList.append(dist2)
        return returnList


# This function is used to find the distance between two points which returns a float value.

def distance(x1, y1, z1, x2, y2, z2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5



def main():

    print(find_intersections(0.0, 0.0, 0.0, 1.52, 3.0, 4.0, 3.0, 1.0, 1.0, 1.0))

    for i in range(datetime.datetime.today().year, 10000):
        year = str(i)
        date = year + year[::-1]
        try:
            datetime.datetime.strptime(date, "%Y%m%d")
            print(date)
        except ValueError:
            pass


main()
