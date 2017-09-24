HERE=`pwd`
LIB_DIR="$(HERE)/lib"
OUTPUT="$(HERE)/business_portal_cache_lambda.zip"

# http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html
package : clean
	pip3 install -r requirements.txt -t $(LIB_DIR)
	zip $(OUTPUT) *.py $(LIB_DIR)/*

clean :
	[ -d $(LIB_DIR) ] && rm -rf $(LIB_DIR) && (rm $(OUTPUT) || true) || true
