.PHONY: clean run 

# run the server
run:
	./manage.py runserver 0.0.0.0:8000

clean:
	find -iname "*.pyc" -delete
 
