#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

/**
* MIT License
* Copyright (c) 2026 revilo111 (github)
*
* Charges battery to target percentage then resets charging value
*
* @param {int} target - The target charge (%) the device aims to reach ( default 95, 0 - 100 )
* @param {int} interval - The time (seconds) between checking if the target has been reached ( default 120, at least 1 )
*
*/

int main(int argc, char **argv) {
	int trg = 95;
	int time = 120;
	if (argc >= 2) {
		trg = strtol(argv[1], NULL, 10);
		if (trg > 100 || trg < 0) {printf("Target charge outside range [0 - 100]\n"); return -1;}
		if (argc >= 3) {
			time = strtol(argv[2], NULL, 10);
			if (time < 1) {printf("Time between checks need to be at least 1\n"); return -1;}
		}
	}
	char *cmd = malloc(sizeof(char)*19);
	strcpy(cmd, "tlp setcharge 0 ");
	char *strg = malloc(sizeof(char)*4);
	sprintf(strg, "%d", trg);
	strcpy(cmd+16, strg);
	system(cmd);
	free(cmd);
	free(strg);

	while(1) {
		FILE *f = fopen("/sys/class/power_supply/BAT1/capacity", "r");
		int chrg;
		fscanf(f, "%d", &chrg);
		fclose(f);
		if ( trg <= chrg ) {
			system("tlp setcharge");
			printf("Stopping charge [%d/%d]\n", chrg, trg);
			return 0;
		}
		printf("Continuing to charge [%d/%d]...\nChecking in %d seconds.\n", chrg, trg, time);
		sleep(time);
	}
	return 0;
}
