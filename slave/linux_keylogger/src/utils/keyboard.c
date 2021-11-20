char* get_me_a_keyboard() {
	struct dirent **namelist;
	int n = 0;
	int i = 0;

	n = scandir(INPUT_EVENT_DIR, &namelist, NULL, alphasort); // read the directory for the files

	if (n == 1) {
		perror("Scandir Failed!!\n");
		exit(EXIT_FAILURE);
	}

	if (n <= 2) {
		perror("No devices found!!\n");
		exit(EXIT_FAILURE);
	}

	//printf("[ * ] %d Devices found !!\n", n - 2);

	for (i = 0; i < n; i++)
		if (namelist[i]->d_name == "." || namelist[i]->d_name == "..") // skip for . and ..
			continue;
		else if (strstr(namelist[i]->d_name, "kbd")) // check if the filename has 'kbd' (keyboard) in it
			break; // if yes, do not look further

	return namelist[i]->d_name; // and return keyboard file name to caller function
}
