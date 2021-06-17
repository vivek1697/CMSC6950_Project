task1.png: task1.py task2.png
	@echo "Running Task-01 to create a csv file and plot for with the intermediate data file"
	@python task1.py

task2.png: task2.py
	@echo "Running Task-02 to create a csv file and plot for with the intermediate data file"
	@python task2.py

clean:
	@echo "Running Cleaning for the files"
	rm *.png
	rm *.csv





