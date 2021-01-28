import math
import sys
sys.path.append(r"F:Drop_Current/DropWithGUI/Lib")
import math
import time

############################################################################
#   Calc Funcs          #
def func(t, x, y, vx, vy):
    g = 32.2
    den = 0.0024
    w = 2.04
    m = w / g
    Cd = 1.6
    A = 45.94 / 144
    Kd = 0.5 * den * A * Cd

    V = math.sqrt(vx ** 2 + vy ** 2)

    dx = vx
    dy = vy
    dvx = -(Kd / m) * V * vx
    dvy = -g - (Kd / m) * V * vy
    dz = [dx, dy, dvx, dvy]
    return dz
def k_set(t, tstep, x, y, vx, vy):
    k1 = func(t, x, y, vx, vy)
    mid_x = x + (k1[0] * tstep) / 2
    mid_y = y + (k1[1] * tstep) / 2
    mid_vx = vx + (k1[2] * tstep) / 2
    mid_vy = vy + (k1[3] * tstep) / 2
    mid = [mid_x, mid_y, mid_vx, mid_vy]

    k2 = func((t + tstep) / 2, mid[0], mid[1], mid[2], mid[3])
    mid_x = x + k2[0] * (tstep) / 2
    mid_y = y + k2[1] * (tstep) / 2
    mid_vx = vx + k2[2] * (tstep) / 2
    mid_vy = vy + k2[3] * (tstep) / 2
    mid = [mid_x, mid_y, mid_vx, mid_vy]

    k3 = func((t + tstep) / 2, mid[0], mid[1], mid[2], mid[3])
    end_x = x + k3[0] * tstep
    end_y = y + k3[1] * tstep
    end_vx = vx + k3[2] * tstep
    end_vy = vy + k3[3] * tstep
    end = [end_x, end_y, end_vx, end_vy]

    k4 = func((t + tstep), end[0], end[1], end[2], end[3])
    phia_x = (k1[0] + 2 * (k2[0] + k3[0]) + k4[0]) / 6
    phia_y = (k1[1] + 2 * (k2[1] + k3[1]) + k4[1]) / 6
    phia_vx = (k1[2] + 2 * (k2[2] + k3[2]) + k4[2]) / 6
    phia_vy = (k1[3] + 2 * (k2[3] + k3[3]) + k4[3]) / 6
    phia = [phia_x, phia_y, phia_vx, phia_vy]

    y2x = x + phia[0] * tstep
    y2y = y + phia[1] * tstep
    y2vx = vx + phia[2] * tstep
    y2vy = vy + phia[3] * tstep

    y2 = [y2x, y2y, y2vx, y2vy]
    return y2
def calc_loop(ti, tf, tstep, x0, y0, vx0, vy0):
    x = x0
    y = y0
    vx = vx0
    vy = vy0
    i = 0
    tt = 0

    while (tt < tf):
        tt = tt + tstep
        i = i + 1
        outs = k_set(tt, tstep, x, y, vx, vy)
        x = outs[0]
        y = outs[1]
        vx = outs[2]
        vy = outs[3]
        if outs[1] < 0:
            # print('Impact in ', outs[0], ' feet')
            # print('Impact in t-minus ', tt, ' Seconds')
            break
        w = [outs[0], tt]
    return outs[0]
def impact_dist_calc(velocity, alt):
    x0 = 0
    y0 = alt
    vx0 = velocity
    vy0 = 0
    ti = 0
    tf = 100
    tstep = .01

    d = calc_loop(ti, tf, tstep, x0, y0, vx0, vy0)
    return d
def v_vector():
        ts = 0.1
        lat0 = cs.lat  # Use param.get thing
        long0 = cs.lng
        time.sleep(ts)
        lat1 = cs.lat
        long1 = cs.lng

        a = (GPS_Coord(lat0, long0))  # Gets manipulatable GPS data
        b = (GPS_Coord(lat1, long1))

        dx = int(b[0]) - int(a[0])  # Gets position changes
        dy = int(b[1]) - int(a[1])
        theta = 0
        if (dx == 0):
            vx = 0
            vy = dy / ts
            theta = math.pi / 2  # 90 or 270

        if (dy == 0):  # add ands for directions
            vx = dx / ts
            vy = 0
            theta = 0  # 0 or 180

        if (dy != 0 & dx != 0):
            vx = dx / ts  # Uses time step to get velocity vector
            vy = dy / ts
            tq = dy / dx
            theta = math.atan(tq)

        return theta, lat1, long1,  # vx, vy

############################################################################
#   Lat & Lon Funcs     #
def dist_to_drop(velocity, alt):
        dist = impact_dist_calc(velocity, alt)
        return dist
def lat_c(lat, theta, dist):
        predicted_lat = lat + (math.cos(theta) * dist) + (cs.airspeed*1*math.cos(theta))
        return predicted_lat
def lon_c(lon, theta, dist):
        predicted_lon = lon + (math.sin(theta) * dist) + (cs.airspeed*1*math.sin(theta))
        return predicted_lon
def GPS_to_ft(coord):
        coordft = coord * 110.574 * 3280.8399
        return coordft
def GPS_Coord(lat, long):
        k = 110.574
        latkm = lat * k
        longkm = long * k
        latft = latkm * 3280.8399
        longft = longkm * 3280.8399
        return tuple([latft, longft])

############################################################################
#   Main, Record        #
def alt_record(alt):
        f = open("Drop_alt.txt", 'a+')
        f.write("Drop alt in feet: %d\r\n" % alt)
        f.close()
def main_loop(pwm):
    a = time.time()
    tspan = 10
    z = 0
    while z < tspan:
        print "in loop"
        t = time.time()
        z = t-a
        n = v_vector()
        lat = n[1]                  #v_vector
        lon = n[2]                  #v_vector
        theta = n[0]

        lat = GPS_to_ft(lat)  # GPS_to_ft(lat)        #make lat and lon into feet
        lon = GPS_to_ft(lon)  # GPS_to_ft(lon)
        velocity = cs.airspeed  # Feet/sec
        altitude = cs.alt  # Feet

        # Get dist to impact
        dist = dist_to_drop(velocity, altitude)
        # Get impact lat & lon
        predicted_lat = lat_c(lat, theta, dist)
        predicted_lon = lon_c(lon, theta, dist)
        # finds dist of impact to target
        drop_dist = (predicted_lat - target_lat) ** 2 + (predicted_lon - target_lon) ** 2
        # Drops if package will hit target & records alt
        if (drop_dist < 30**2):
            print('Hits in Range')
            Script.SendRC(6, pwm, True)
            print(altitude)
            alt_record(altitude)
            break

        # Emergency Signal and recording
        t_emergency = tspan - .5
        if (z >= t_emergency ):
            print('Use Emergency Drop')
            alt_record(altitude)
            break

        # Continues looping when no hit is found
        else:
            print('Did not hit')
            #el = time.time() - t
            # print(el)
    pass

############################################################################
#   GUI Setup           #
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
from System.Drawing import Point
from System.Windows.Forms import Application, Button, Form, Label, TextBox
class SimpleTextBoxForm(Form):
    def __init__(self):
        self.Text = "UTM Auto Package Release"
        self.Width = 400
        self.Height = 300

        self.label = Label()
        self.label.Text = "Drop Altitude"
        self.label.Location = Point(25, 200)
        self.label.Height = 50
        self.label.Width = 250

        self.textbox = TextBox()
        self.textbox.Text = "The Default Text"
        self.textbox.Location = Point(25, 75)
        self.textbox.Width = 150

        self.button1 = Button()
        self.button1.Text = 'Run 1 Start'
        self.button1.Location = Point(25, 50)
        self.button1.Click += self.d_runL           #Main while 1

        self.button2 = Button()
        self.button2.Text = 'Run 2 Start'
        self.button2.Location = Point(25, 75)
        self.button2.Click += self.d_runR           #Main while 2

        self.button3 = Button()
        self.button3.Text = 'Emergency Drop Left'
        self.button3.Location = Point(125, 50)
        self.button3.Width = 200
        self.button3.Click += self.e_dropL          #Drop Left and Record

        self.button4 = Button()
        self.button4.Text = 'Emergency Drop Right'
        self.button4.Location = Point(125, 75)
        self.button4.Width = 200
        self.button4.Click += self.e_dropR          #Drop Right and Record

        self.button5 = Button()
        self.button5.Text = 'Emergency Drop All'
        self.button5.Location = Point(125, 125)
        self.button5.Width = 200
        self.button5.Click += self.e_drop_all        #Drop All and Record

        self.AcceptButton = self.button1
        self.AcceptButton = self.button2
        self.CancelButton = self.button3
        self.CancelButton = self.button4
        self.CancelButton = self.button5

        self.Controls.Add(self.label)
        self.Controls.Add(self.button1)
        self.Controls.Add(self.button2)
        self.Controls.Add(self.button3)
        self.Controls.Add(self.button4)
        self.Controls.Add(self.button5)

    left = 1400
    right = 1600

    #Run Main
    def d_runL(self, sender, event):
        main_loop(1400)
        x = str(100)
        self.label.Text = x

    def d_runR(self, sender, event):
        main_loop(1600)

    #Interupt and Drop Side
    def e_dropL(self, sender, event):
        Script.SendRC(6, 1400, True)
        alt_record(cs.alt)

    def e_dropR(self, sender, event):
        Script.SendRC(6, 1600, True)
        alt_record(cs.alt)

    #Interupt and Drop Both
    def e_drop_all(self, sender, event):
        alt_record(cs.alt)
        Script.SendRC(6, 1400, True)
        time.sleep(0.15)
        Script.SendRC(6, 1600, True)
        time.sleep(0.15)

############################################################################
#   Program Start       #
target_lat = 36.52527
target_lon = -88.91543
target_lat = GPS_to_ft(target_lat)
target_lon = GPS_to_ft(target_lon)

#   Start GUI           #
#f = threading.Thread(target= SimpleTextBoxForm)
#f.start()
f = SimpleTextBoxForm()
Application.Run(f)