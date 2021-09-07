
import speedtest

def main():
    wifi  = speedtest.Speedtest()
    print("Wifi Download Speed is ", wifi.download())
    print("Wifi Upload Speed is ", wifi.upload())



if __name__ == "__main__":
    main()