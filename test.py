if __name__ == "__main__":
    import matlab
    import matlab.engine
    engine = matlab.engine.start_matlab()
    content = engine.sqrt(2.)
    print(content)
