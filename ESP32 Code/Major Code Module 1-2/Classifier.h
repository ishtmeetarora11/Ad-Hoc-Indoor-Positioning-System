#pragma once
#include <cstdarg>
namespace Eloquent {
    namespace ML {
        namespace Port {
            class DecisionTree {
                public:
                    /**
                    * Predict class for features vector
                    */
                    int predict(float *x) {
                        if (x[2] <= -44.5) {
                            return 0;
                        }

                        else {
                            if (x[1] <= -77.5) {
                                if (x[1] <= -91.5) {
                                    if (x[0] <= -57.0) {
                                        if (x[5] <= -46.5) {
                                            return 1;
                                        }

                                        else {
                                            if (x[1] <= -93.0) {
                                                return 1;
                                            }

                                            else {
                                                return 0;
                                            }
                                        }
                                    }

                                    else {
                                        return 1;
                                    }
                                }

                                else {
                                    return 1;
                                }
                            }

                            else {
                                if (x[0] <= -55.5) {
                                    if (x[1] <= -70.5) {
                                        return 3;
                                    }

                                    else {
                                        if (x[1] <= -32.0) {
                                            if (x[1] <= -69.5) {
                                                if (x[0] <= -64.0) {
                                                    return 2;
                                                }

                                                else {
                                                    if (x[0] <= -61.5) {
                                                        if (x[0] <= -62.5) {
                                                            return 3;
                                                        }

                                                        else {
                                                            return 2;
                                                        }
                                                    }

                                                    else {
                                                        return 3;
                                                    }
                                                }
                                            }

                                            else {
                                                if (x[1] <= -65.5) {
                                                    if (x[1] <= -68.5) {
                                                        return 2;
                                                    }

                                                    else {
                                                        if (x[0] <= -60.0) {
                                                            if (x[1] <= -66.5) {
                                                                return 2;
                                                            }

                                                            else {
                                                                if (x[0] <= -63.0) {
                                                                    return 3;
                                                                }

                                                                else {
                                                                    return 2;
                                                                }
                                                            }
                                                        }

                                                        else {
                                                            return 3;
                                                        }
                                                    }
                                                }

                                                else {
                                                    if (x[0] <= -65.5) {
                                                        if (x[0] <= -66.5) {
                                                            return 2;
                                                        }

                                                        else {
                                                            return 3;
                                                        }
                                                    }

                                                    else {
                                                        return 2;
                                                    }
                                                }
                                            }
                                        }

                                        else {
                                            if (x[5] <= -47.0) {
                                                return 1;
                                            }

                                            else {
                                                return 0;
                                            }
                                        }
                                    }
                                }

                                else {
                                    if (x[1] <= -65.5) {
                                        if (x[1] <= -69.5) {
                                            if (x[1] <= -75.5) {
                                                if (x[0] <= -20.0) {
                                                    return 3;
                                                }

                                                else {
                                                    return 2;
                                                }
                                            }

                                            else {
                                                return 3;
                                            }
                                        }

                                        else {
                                            if (x[1] <= -68.5) {
                                                if (x[0] <= -15.0) {
                                                    if (x[0] <= -47.5) {
                                                        return 3;
                                                    }

                                                    else {
                                                        if (x[0] <= -37.0) {
                                                            return 2;
                                                        }

                                                        else {
                                                            return 3;
                                                        }
                                                    }
                                                }

                                                else {
                                                    return 2;
                                                }
                                            }

                                            else {
                                                if (x[0] <= -53.5) {
                                                    if (x[1] <= -66.5) {
                                                        if (x[1] <= -67.5) {
                                                            if (x[0] <= -54.5) {
                                                                return 3;
                                                            }

                                                            else {
                                                                return 2;
                                                            }
                                                        }

                                                        else {
                                                            return 3;
                                                        }
                                                    }

                                                    else {
                                                        return 2;
                                                    }
                                                }

                                                else {
                                                    return 3;
                                                }
                                            }
                                        }
                                    }

                                    else {
                                        if (x[1] <= -32.5) {
                                            if (x[0] <= -18.5) {
                                                if (x[0] <= -45.5) {
                                                    if (x[0] <= -54.5) {
                                                        return 2;
                                                    }

                                                    else {
                                                        if (x[0] <= -53.0) {
                                                            return 3;
                                                        }

                                                        else {
                                                            return 2;
                                                        }
                                                    }
                                                }

                                                else {
                                                    return 3;
                                                }
                                            }

                                            else {
                                                return 2;
                                            }
                                        }

                                        else {
                                            if (x[0] <= -48.5) {
                                                if (x[0] <= -49.5) {
                                                    return 0;
                                                }

                                                else {
                                                    return 1;
                                                }
                                            }

                                            else {
                                                return 0;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }

                    /**
                    * Predict readable class name
                    */
                    const char* predictLabel(float *x) {
                        return idxToLabel(predict(x));
                    }

                    /**
                    * Convert class idx to readable name
                    */
                    const char* idxToLabel(uint8_t classIdx) {
                        switch (classIdx) {
                            case 0:
                            return "Exit 1";
                            case 1:
                            return "Garden";
                            case 2:
                            return "Courtyard";
                            case 3:
                            return "The Great Hall";
                            default:
                            return "Ishtmeet we have a problem";
                        }
                    }

                protected:
                };
            }
        }
    }
