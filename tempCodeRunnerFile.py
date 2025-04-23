WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "buttonBegin")))