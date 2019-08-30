package lib

func InArray(val string, arr []string) bool {
	if len(val) == 0 || len(arr) == 0 {
		return false
	}
	for _,v := range arr  {
		if v == val {
			return true
		}
	}
	return false;
}