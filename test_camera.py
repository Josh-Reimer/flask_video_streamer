#!/usr/bin/env python3
"""
Simple camera test script to verify camera functionality
before running the main Flask video streaming application.
"""

import cv2
import time
from imutils.video import VideoStream

def test_camera():
    print("Testing camera functionality...")
    
    # Try PiCamera first
    try:
        print("Attempting to use PiCamera...")
        vs = VideoStream(usePiCamera=1).start()
        time.sleep(2.0)
        
        # Try to read a few frames
        for i in range(5):
            frame = vs.read()
            if frame is not None:
                print(f"PiCamera frame {i+1}: {frame.shape}")
            else:
                print(f"PiCamera frame {i+1}: None")
            time.sleep(0.5)
        
        vs.stop()
        print("PiCamera test completed successfully!")
        return True
        
    except Exception as e:
        print(f"PiCamera failed: {e}")
        
        # Try USB camera
        try:
            print("Attempting to use USB camera...")
            vs = VideoStream(src=0).start()
            time.sleep(2.0)
            
            # Try to read a few frames
            for i in range(5):
                frame = vs.read()
                if frame is not None:
                    print(f"USB camera frame {i+1}: {frame.shape}")
                else:
                    print(f"USB camera frame {i+1}: None")
                time.sleep(0.5)
            
            vs.stop()
            print("USB camera test completed successfully!")
            return True
            
        except Exception as e:
            print(f"USB camera failed: {e}")
            return False

if __name__ == "__main__":
    success = test_camera()
    if success:
        print("\nCamera test PASSED. You can now run the main application.")
    else:
        print("\nCamera test FAILED. Please check your camera setup.")
