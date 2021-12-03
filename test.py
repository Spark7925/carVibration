import matlab
import matlab.engine

if __name__ == "__main__":

    engine = matlab.engine.start_matlab()
    ans = engine.middle_example()
    print(ans)

