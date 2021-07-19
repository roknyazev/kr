//
// Created by romak on 25.05.2021.
//

#include "UAV.h"

void UAV::setType(UAV::hubType t)
{
	type = t;

	if (type == smallHub)
	{
		meanV = 20 * 2;
	}

	else if (type == mediumHub)
	{
		meanV = 100 * 2;
	}

	else
	{
		meanV = 500 * 2;
	}
}

double UAV::getMeanV() const
{
	return this->meanV;
}
