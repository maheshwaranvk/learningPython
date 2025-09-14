class FileOperation:
    with open("./week3/classroom/report.txt", "a") as f:
        f.write("\nTestCase4 - Passed\n")
        f.write("TestCase5 - Failed")
    with open("./week3/classroom/report.txt", "r") as f1:
        content = f1.readlines()
        print(content)
        passed = 0
        failed = 0
        for line in content:
            if line.count("Passed"):
                passed=passed+1
            else:
                failed=failed+1      
        print ("Total Testcases", len(f1.read()))
        print ("Passed", passed)
        print ("Failed", failed)