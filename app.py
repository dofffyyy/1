from flask import Flask, render_template, request
#from  gpiozero import Robot
from time import sleep

app = Flask(__name__)

# Set up GPIO pins for motor control
#robot = Robot(left = (7, 8), right = (9, 10))



# This function controls the robot's movement
def move_robot(direction):
    if direction == 'forward':  #landmark 1
        '''robot.forward()
        sleep(3)
        robot.stop()
        sleep(3)
        robot.right()
        sleep(1)
        robot.right()
        sleep(1)
        robot.forward()
        sleep(3)
        robot.right()
        sleep(1)
        robot.right()
        robot.stop()'''
        sleep(5)
    elif direction == 'backward':  #landmark 2
        '''robot.left()
        robot.forward()
        sleep(3)
        robot.stop()
        sleep(3)
        robot.right()
        robot.right()
        sleep(1)
        robot.forward()
        sleep(3)
        robot.left()
        sleep(1)
        robot.stop()'''
        sleep(5)
    elif direction == 'left':   #landmark 3
        '''robot.right()
        robot.right()
        robot.forward()
        sleep(3)
        robot.stop()
        sleep(3)
        robot.right()
        robot.right()
        sleep(1)
        robot.forward()'''
        sleep(5)
    elif direction == 'right':
        '''robot.right()
        robot.forward()
        sleep(3)
        robot.stop()
        sleep(3)
        robot.right()
        robot.right()
        sleep(1)
        robot.forward()
        sleep(3)
        robot.right()
        sleep(2)
        robot.stop()'''
        sleep(5)
    else:
        #robot.stop()
        sleep(5)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    direction = data['direction']
    move_robot(direction)  # Call the move_robot function without returning a response
    return '', 204  # Return an empty response with 204 No Content status code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
